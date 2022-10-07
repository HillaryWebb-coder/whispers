from django import template

register = template.Library()


@register.simple_tag
def whisper_likes(whisper):
    return whisper.likes.filter(liked=True)


@register.simple_tag
def user_liked_whisper(user, whisper_likes):
    return whisper_likes.filter(user=user.id)
