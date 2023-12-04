from typing import Any, Dict, Sequence
from django.forms import BaseModelForm
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin
from django.db.models import QuerySet


from .models import Preset, PresetImage
from .forms import PresetForm, FilterForm
from .validators.validators import valid_image_size


class PresetListView(FormMixin, ListView):
    model = Preset
    paginate_by = 15
    form_class = FilterForm

    def get_ordering(self) -> Sequence[str]:
        SORTING_FILTER = self.request.GET.get("sort_by")
        
        if SORTING_FILTER:
            if SORTING_FILTER == "Newest":
                return "-created_at"
            elif SORTING_FILTER == 'Oldest':
                return "created_at"
            elif SORTING_FILTER == 'Likes':
                return "-like_count"
            elif SORTING_FILTER == 'Downloads':
                return "-download_count"
            elif SORTING_FILTER == 'Views':
                return "-view_count"
            
            return "-created_at"
        else:
            return "-created_at"

    def get_queryset(self) -> QuerySet[Any]:
        CHARACTER_FILTER = self.request.GET.get('character')

        queryset = super().get_queryset()
        if CHARACTER_FILTER:
            return queryset.filter(character=CHARACTER_FILTER)
        else:
            return queryset


class PresetDetailView(DetailView):
    model = Preset
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        preset = context['preset']

        context['additional_thumbnails'] = preset.additional_thumbnail_files.all()

        if preset.user_who_submitted.id == self.request.user.id:
            context['is_owner'] = True
        
        return context


class PresetCreateView(CreateView):
    model = Preset
    template_name = "presets/preset_create_form.html"
    form_class = PresetForm
    success_url = "/"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        preset = form.save(commit=False)

        preset.user_who_submitted = self.request.user
        preset.save()

        preset.likes.add(self.request.user)
        preset.like_count += 1

        additional_thumbnail_files = self.request.FILES.getlist('additional_thumbnail_files')
        for thumbnail_file in additional_thumbnail_files:
            preset_image = PresetImage.objects.create(image=thumbnail_file)
            preset.additional_thumbnail_files.add(preset_image)
            preset.save()
        
        messages.success(self.request, message='Preset was successfully created!')
        return redirect("presets:index")


@login_required
def delete(request, preset_id):
    if request.POST:
        Preset.objects.select_for_update().filter(id=preset_id).delete()
        messages.success(request, "Preset successfully deleted!")
        return redirect("presets:index")
    else:
        messages.error(request, 'Error occurred trying to delete preset!')
        return redirect("presets:detail", preset_id=preset_id)


@login_required
def like(request, preset_id):
    if request.POST:
        # Get the actual preset and user objects
        preset = Preset.objects.get(id=preset_id)
        user = User.objects.get(id=request.user.id)

        # Add user to the preset's 'likes' table
        preset.likes.add(user)

        # Increment preset's like count
        preset.like_count += 1
        preset.save()

        success_message = "Preset liked! View liked presets on your account page!"
        messages.success(request, success_message)
        return redirect("presets:detail", id=preset_id)
    else:
        messages.error(request, "Error occurred trying to like preset!")
        return redirect("presets:index")


@login_required
def remove_like(request, preset_id):
    if request.POST:
        # Get the actual preset and user objects
        preset = Preset.objects.get(id=preset_id)
        user = User.objects.get(id=request.user.id)

        # Remove user to the preset's 'likes' table
        preset.likes.remove(user)

        # Decrement preset's like count
        preset.like_count -= 1
        preset.save()

        messages.success(request, "Like removed from preset!")
        return redirect("presets:detail", id=preset_id)
    else:
        messages.error(request, "Error occurred trying to like preset!")
        return redirect("presets:index")


@login_required
def download(request, preset_id):
    if request.POST:
        # Get the preset
        preset = Preset.objects.get(id=preset_id)

        # Increment preset's save counter
        preset.download_count += 1

        preset.save()

        # Open the preset's zip file, read as binary
        return FileResponse(open(preset.zip_file.path, "rb"))
    else:
        messages.error(request, "Error occurred trying to download preset!")
        return redirect("presets:index")


@login_required
def account(request, user_id):
    PRESETS_PER_PAGE = 12

    user = User.objects.get(id=user_id)
    liked_presets = Preset.objects.filter(likes__exact=user_id)

    total_likes, total_downloads, total_views = 0, 0, 0

    for preset in liked_presets:
        if preset.user_who_submitted == user:
            total_likes += preset.like_count
            total_downloads += preset.download_count
            total_views += preset.view_count

    paginator = Paginator(liked_presets, PRESETS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'liked_presets': liked_presets,
        'page_obj': page_obj,
        'curr_user': user,
        'total_likes': total_likes,
        'total_downloads': total_downloads,
        'total_views': total_views
    }

    if user_id == request.user.id:
        context['is_owner'] = True

    return render(request, 'presets/account.html', context)


@login_required
def update(request, preset_id):
    """
    View for updating a preset.

    If a POST is sent, it will try to update the preset with the given data.

    Params:
        preset_id -> ID of preset to be updated
    """
    context = {}
    preset_to_update = get_object_or_404(Preset, pk=preset_id)

    # Checks if the user owns the preset and redirects if not
    if preset_to_update.user_who_submitted.id != request.user.id:
        messages.error(request, 'This preset cannot be updated by the current user.')
        return redirect("presets:detail", id=preset_id)

    form = PresetForm(
        request.POST or None,
        request.FILES or None,
        instance=preset_to_update
    )
    
    if request.POST:
        if form.is_valid():
            preset = form.save(commit=False)

            new_thumbnail_files = request.FILES.getlist('additional_thumbnail_files')

            # Get current thumbnail files, delete them, and then add the new ones
            # Current thumbnails
            if new_thumbnail_files != []:
                # Validate each thumbnail because ModelForm won't do it
                try:
                    for thumbnail_file in new_thumbnail_files:
                        valid_image_size(thumbnail_file)
                except ValidationError as e:
                    context['form'] = form
                    context['preset'] = preset_to_update
                    messages.error(request, e.message)
                    return render(request, 'presets/update.html', context)

                current_thumbnail_files = preset.additional_thumbnail_files.all()

                for thumbnail_file in current_thumbnail_files:
                    thumbnail_file.delete()

            # New thumbnails
            for thumbnail_file in new_thumbnail_files:
                preset_image = PresetImage.objects.create(image=thumbnail_file)
                preset.additional_thumbnail_files.add(preset_image)

            preset.save()
            
            messages.success(request, 'Preset was successfully updated!')
            return redirect("presets:detail", id=preset_id)
        else:
            context['form'] = form
            context['preset'] = preset_to_update
            messages.error(request, 'Preset was not updated!')
            return render(request, 'presets/update.html', context)
    else:
        context['form'] = form
        context['preset'] = preset_to_update
        return render(request, 'presets/update.html', context)


@staff_member_required
def generate_presets(request):
    """
    Generates 100 random test presets.
    """
    number = 1
    while number <= 100:
        Preset.objects.create(
            name="Test Preset #{}".format(number),
            description="Test preset #{}'s description".format(number),
            user_who_submitted=request.user
        )

        number += 1
    
    return redirect("presets:index")


@staff_member_required
def delete_presets(_):
    """
    Deletes all current presets.
    """
    Preset.objects.all().delete()
    return redirect("presets:index")


class AboutView(TemplateView):
    template_name = "presets/about.html"


class ChangelogView(TemplateView):
    template_name = "presets/changelog.html"
