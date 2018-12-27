from django.conf import settings

def title_subtitle(request):
    return {'TITLE' : settings.SITE_TITLE, 'SUBTITLE': settings.SITE_SUBTITLE}