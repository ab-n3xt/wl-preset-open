from django.core.exceptions import ValidationError

from zipfile import is_zipfile

MEGABYTE = 1048576
FIVE_MEGABYTES = 5242880

def valid_preset_size(file):
    limit = MEGABYTE
    if file.size > limit:
        raise ValidationError('Preset zip is too large. Preset zip should not exceed 1 MB.')

def valid_image_size(file):
    limit = FIVE_MEGABYTES
    if file.size > limit:
        raise ValidationError('Image file is too large. Image file size should not exceed 5 MB.')

def valid_zip(file):
    if not is_zipfile(file):
        raise ValidationError('File is not a valid zip file.')