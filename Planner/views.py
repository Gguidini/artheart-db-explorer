from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

def index(request):
    data = {}
    return render(request, 'Planner/index.html', data)