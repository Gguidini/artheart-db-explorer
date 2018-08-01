from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

def index(request):
    if request.user.is_authenticated:
        data = {}
        return render(request, 'Planner/index.html', data)
    else:
        return redirect(reverse_lazy('url_login'))