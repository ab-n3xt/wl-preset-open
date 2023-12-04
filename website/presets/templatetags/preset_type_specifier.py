from django import template

register = template.Library()

@register.filter(name='get_character_name')
def get_character_name(preset):
    return preset.Character(preset.character).label