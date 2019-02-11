from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from ArtHeart.settings import MEDIA_URL

def index(request):
    data = {}
    return render(request, 'Planner/index.html', data)