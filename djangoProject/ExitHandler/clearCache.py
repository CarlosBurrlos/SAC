from django.core.cache import cache

def removeAll():
    cache.clear()