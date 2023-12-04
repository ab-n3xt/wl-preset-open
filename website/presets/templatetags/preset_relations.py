from django import template

register = template.Library()

# https://stackoverflow.com/a/32615427
# To check if a relationship exists within a template
@register.filter(name='check_if_preset_liked')
def check_if_preset_liked(preset, user):
    user_id = int(user.id)
    return preset.likes.filter(id=user_id).exists()
