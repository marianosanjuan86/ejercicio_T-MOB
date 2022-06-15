from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse


def index (request):    
    key_a_buscar = request.GET.get('key', '')
    return HttpResponse (cache.get(key_a_buscar))


