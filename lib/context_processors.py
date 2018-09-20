from django.utils.module_loading import import_string
from django.conf import settings
from apps.blog.models import Post

MENU = []

def get_menu_for_app(app_name):
    name = f'{app_name}.urls.menu'
    try:
        return import_string(name)
    except ImportError:
        return []

for app in settings.INSTALLED_APPS:
    MENU += get_menu_for_app(app)

def total_posts(request):
    return {
        'total_posts': Post.objects.all().count() 
    }

def navbar(request):
    return { 'nav_menu': MENU }