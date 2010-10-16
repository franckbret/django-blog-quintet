"""Settings of Zinnia"""
from django.conf import settings

MEDIA_URL = getattr(settings, 'BLOGQUINTET_MEDIA_URL', '/blogquintet/')
