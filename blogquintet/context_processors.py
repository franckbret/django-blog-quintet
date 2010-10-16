"""Context Processors for blogquintet"""
from blogquintet.settings import MEDIA_URL


def media(request):
    """Adds media-related context variables to the context"""
    return {'BLOGQUINTET_MEDIA_URL': MEDIA_URL}

