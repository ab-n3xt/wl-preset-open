from django import forms

from .models import Preset

from .validators.validators import valid_image_size


class PresetForm(forms.ModelForm):
    additional_thumbnail_files = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        validators=[valid_image_size],
        help_text="Maximum 5MB per image",
        label="Addtional images for the preset"
    )

    def __init__(self, *args, **kwargs):
        super(PresetForm, self).__init__(*args, **kwargs)
        self.fields['zip_file'].widget.attrs.update({
            'accept': 'application/zip'
        })
        self.fields['character'].choices = self.fields['character'].choices[1:]

    class Meta:
        model = Preset
        fields = [
            'name',
            'description',
            'character',
            'zip_file',
            'thumbnail_file',
            'additional_thumbnail_files'
        ]
        labels = {
            'name': "Name of preset",
            'description': "Description of preset",
            'zip_file': "Zip file with the preset contents",
            'thumbnail_file': "Main image for the preset",
        }
        widgets = {
            'description': forms.Textarea,
        }
        help_texts = {
            'name': "Maximum 30 characters",
            'description': "Maximum 820 characters",
            'zip_file': "Maximum 1MB",
            'thumbnail_file': "Maximum 5MB",
        }


class FilterForm(forms.ModelForm):
    sort_choices = (
        ('Newest', 'Newest'),
        ('Oldest', 'Oldest'),
        ('Likes', 'Most Liked'),
        ('Downloads', 'Most Downloaded'),
        ('Views', 'Most Viewed')
    )
    sort_by = forms.ChoiceField(choices=sort_choices)
    
    class Meta:
        model = Preset
        fields = ['character']
        labels = {
            'character': "Character to filter by"
        }