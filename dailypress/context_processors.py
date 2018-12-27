from django.conf import settings
from datetime import datetime

def title_subtitle(request):
    return {'TITLE' : settings.SITE_TITLE, 'SUBTITLE': settings.SITE_SUBTITLE, 'TIME': datetime.now()}