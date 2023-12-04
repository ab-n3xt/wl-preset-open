from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db.utils import IntegrityError
from django.contrib import messages

from .forms import LoginForm, EditUserForm


def login_user(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in!")
                return HttpResponseRedirect('/')

            # User doesn't exist; return to login page with error
            context['form'] = LoginForm()
            messages.error(request, "The username/password either don't match or exist.")
            return render(request, 'users/login.html', context)
    else:
        form = LoginForm()
        context['form'] = form
        return render(request, 'users/login.html', context)


def create_user(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                # Create new user
                # Throws IntegrityError if the username is taken
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )

                if user is not None:
                    # Save to database, then login the user
                    user.save()
                    login(request, user)
                    messages.success(request, "Welcome " + user.get_username() + "!")
                    return redirect("presets:index")

                context['form'] = LoginForm()
                messages.error(request, 'Creating the account was unsuccessful.')
                return render(request, 'users/login.html', context)
            except IntegrityError:
                context['form'] = form
                messages.error(request, 'Username taken. Please choose a different username.')
                return render(request, 'users/login.html', context)
    else:
        form = LoginForm()
        context['form'] = form
        return render(request, 'users/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out!")
    return HttpResponseRedirect('/')    


@login_required
def edit_user(request):
    context = {}
    if request.POST:
        form = EditUserForm(request.POST)
        if form.is_valid():
            try:
                current_password = form.cleaned_data['password']
                
                # If old password is not correct, raise IntegrityError
                if not check_password(current_password, request.user.password):
                    raise IntegrityError

                # Get current user from the database
                current_user = User.objects.get(pk=request.user.id)
                if current_user:
                    current_user.set_password(form.cleaned_data['new_password'])
                    current_user.save()

                    messages.success(request, 'Password change successful!')
                    return redirect('presets:account', user_id=request.user.id)

                context['form'] = EditUserForm()
                messages.error(request, 'Changing password was unsuccessful.')
                return render(request, 'users/edit.html', context)
            except IntegrityError:
                context['form'] = form
                messages.error(request, f'Old password incorrect. Password has not changed.')
                return render(request, 'users/edit.html', context)
    else:
        form = EditUserForm()
        context['form'] = form
        return render(request, 'users/edit.html', context)


@login_required
def delete_user(request):
    if request.POST:
        try:
            user_from_db = User.objects.get(pk=request.user.id)
            user_from_db.delete()
            messages.success(request, "Your account has been successfully deleted.")
            return redirect("presets:index")
        except User.DoesNotExist:
            messages.error(request, "The user does not exist and therefore, cannot be deleted.")
            return redirect("presets:index")
        except:
            messages.error(request, "There was an error trying to delete your account.")
            return redirect("presets:index")
    else:
        return render(request, 'users/delete.html')