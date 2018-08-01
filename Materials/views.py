from django.shortcuts import render, HttpResponse, redirect
from .models import Apostila, Project, Categoria
from django.urls import reverse_lazy

from ArtHeart.settings import MEDIA_ROOT
import os
from .forms import ApostilaUpload, ProjectUpload

# Create your views here.
def search(request):
    data = {}
    projs = Project.objects.all()
    cats = Categoria.objects.all()
    data['projects'] = projs
    data['categories'] = cats
    aps = Apostila.objects.all()
    # filter entries to be displayed
    if request.method == 'GET' and not request.GET == {}:
        if 'search' in request.GET:
            search = request.GET['search']
            aps = aps.filter(title__icontains=search)
        if 'project' in request.GET:
            proj = request.GET['project']
            if proj != '':
                aps = aps.filter(project=proj)
        if 'categories' in request.GET:
            cats = request.GET.getlist('categories')
            aps = aps.filter(categories__in=cats)
    data['entries'] = aps
    return render(request, 'Materials/search.html', data)

def detail(request, pk):
    pk = int(pk)
    if request.method == 'GET':
        if pk != -1:
            ap = Apostila.objects.get(pk=pk)
            form = ApostilaUpload(instance=ap)
            data = {'doc':ap, 'form':form, 'edit':True }
        else:
            form = ApostilaUpload()
            data = { 'form':form, 'edit':False }
        return render(request, 'Materials/detail.html', data)
    else:
        if pk != -1:
            if 'file-clear' in request.POST or 'file' in request.FILES:
                deleteFile(pk)
            form = ApostilaUpload(request.POST or None, request.FILES or None, instance=Apostila.objects.get(pk=pk))
        else:
            form = ApostilaUpload(request.POST or None, request.FILES or None)
        if form.is_valid() :
            entry = form.save()
            cats = request.POST.getlist('categories')
            selected = []
            for c in cats:
                selected.append(Categoria.objects.get(pk=c))

            entry.categories.set(selected)
            entry.save()
            return redirect(reverse_lazy('url_search'))
        else:
            data = {'form':form}
            if pk != -1:
                data['doc'] = Apostila.objects.get(pk=pk)
                data['edit'] = True
            else:
                data['edit'] = False
            return render(request, 'Materials/details.html', )

def projects(request):
    data = {}
    data['projects'] = Project.objects.all()
    data['form'] = ProjectUpload()
    if request.method == 'POST':
        form = ProjectUpload(request.POST or None)
        if form.is_valid():
            form.save()
        data['projects'] = Project.objects.all()
        data['form'] = form
        return render(request, 'Materials/projects.html', data)
    else:
        return render(request, 'Materials/projects.html', data)
        
def deleteFile(pk):
    ap = Apostila.objects.get(pk=pk)
    try:
        os.remove(os.path.join(MEDIA_ROOT, str(ap.file)))
    except:
        pass # silence error when no file is there

def delete(request, pk):
    """
    Deleta uma Apostila do banco de dados e qualquer arquivo referênciado por ele.
    """
    if request.user.is_authenticated:
        doc = Apostila.objects.get(pk=pk)
        deleteFile(pk)
        doc.delete()
        return redirect('url_search')