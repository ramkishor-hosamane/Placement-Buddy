from django import template
from django.http import HttpResponse
from Home.models import User
register = template.Library()


def is_starred(fav_posts,logined_user):
    print(logined_user,fav_posts)
    user_obj = User.objects.get(name=logined_user)
    if len(fav_posts.filter(user=user_obj)):
        return 'checked'
    return ''
register.filter('is_starred',is_starred)