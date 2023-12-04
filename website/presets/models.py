from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .validators.validators import valid_preset_size, valid_image_size, valid_zip

class PresetImage(models.Model):
    image = models.ImageField(
        upload_to='images',
        validators=[valid_image_size]
    )


class Preset(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=820)
    zip_file = models.FileField(
        upload_to='zip_files',
        validators=[valid_preset_size, valid_zip],
        default='zip_files/default.zip'
    )
    thumbnail_file = models.ImageField(
        upload_to='images',
        validators=[valid_image_size],
        default='images/default.jpg'
    )
    created_at = models.DateTimeField(
        db_index=True, 
        default=timezone.now
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    # User who submitted the preset
    user_who_submitted = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Other thumbnails
    additional_thumbnail_files = models.ManyToManyField(PresetImage)

    # Counts for stats purposes
    like_count = models.IntegerField(default=0)
    download_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)

    # Enum for preset's character type
    class Character(models.TextChoices):
        ALL = 'ALL'
        AOI = 'AOI'
        BOL = 'BOL'
        BORCO = 'BORCO'
        CHAKKAR = 'CHAKKAR'
        CORMAN = 'CORMAN'
        EMMA = 'EMMA'
        ILJAH = 'ILJAH'
        INDRA = 'INDRA'
        JADEEN = 'JADEEN'
        JENNY = 'JENNY'
        KIM = 'KIM'
        KRAL = 'KRAL'
        LALA = 'LALA'
        LEAH = 'LEAH'
        LEE = 'LEE'
        LYNDON = 'LYNDON'
        MAX = 'MAX'
        MAYA = 'MAYA'
        MERCER = 'MERCER'
        MILANNA = 'MILANNA'
        MINOTAUR = 'MINOTAUR'
        MORRIS = 'MORRIS'
        NERO_NERO = 'NERO_NERO'
        RAWN = 'RAWN'
        SERENIA = 'SERENIA'
        SHANNON = 'SHANNON'
        SHEY = 'SHEY'
        SHEYFUTA = 'SHEYFUTA'
        SHIVA = 'SHIVA'
        SONIA = 'SONIA'
        TANYA = 'TANYA'
        TRIBALMALEA1 = 'TRIBALMALEA1'
        ZIAD = 'ZIAD'
        OTHER = 'OTHER'

    character = models.CharField(
        max_length=12,
        choices=Character.choices,
        default=Character.ALL,
    )

    # Additional tables to link users to presets
    likes = models.ManyToManyField(User, related_name="preset_likes")

    def __str__(self):
        return self.name