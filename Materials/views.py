"""
This file defines functions to manipulate user interaction with the web-interface.

Responsible for views related to the models defined in Materials/models.py.
"""

from django.shortcuts import render, HttpResponse, redirect
from .models import Apostila, Project, Categoria
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from ArtHeart.settings import MEDIA_ROOT, MEDIA_URL
import os
from .forms import ApostilaUpload, ProjectUpload, CategoryUpload

# Create your views here.


def search(request):
    """
    Shows all available Apostilas.
    It's possible to search by title, category, and project.

    Template for this view is 'Materials/seatch.html'
    Links to detail view.
    """
    data = {}
    projs = Project.objects.all()
    cats = Categoria.objects.all()
    data['projects'] = projs
    data['categories'] = cats
    data['media'] = MEDIA_URL
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
    """
    Edit existing Apostila or add new one.
    On successful operation, returns to search view.

    Template for this view is 'Materials/detail.html'
    """
    pk = int(pk)
    if request.method == 'GET':
        if pk != -1:
            ap = Apostila.objects.get(pk=pk)
            form = ApostilaUpload(instance=ap)
            data = {'doc': ap, 'form': form, 'edit': True}
        else:
            form = ApostilaUpload()
            data = {'form': form, 'edit': False}
        return render(request, 'Materials/detail.html', data)
    else:
        if pk != -1:
            if 'file-clear' in request.POST or 'file' in request.FILES:
                deleteFile(pk)
            form = ApostilaUpload(
                request.POST or None, request.FILES or None, instance=Apostila.objects.get(pk=pk))
        else:
            form = ApostilaUpload(
                request.POST or None, request.FILES or None)
        if form.is_valid():
            entry = form.save()
            cats = request.POST.getlist('categories')
            projects = request.POST.getlist('project')
            selected = []
            for c in cats:
                selected.append(Categoria.objects.get(pk=c))
            entry.categories.set(selected)
            selected = []
            for p in projects:
                selected.append(Project.objects.get(pk=p))
            entry.project.set(selected)
            entry.save()
            return redirect(reverse_lazy('url_search'))
        else:
            data = {'form': form}
            if pk != -1:
                data['doc'] = Apostila.objects.get(pk=pk)
                data['edit'] = True
            else:
                data['edit'] = False
            return render(request, 'Materials/details.html', )


def projects(request):
    """
    Shows available Projects. Also possible to add new Project.
    Quick glance at Project's title, client, and state of completion.
    User that are not authenticated CANNOT create new projects

    Template for this view is 'Materials/projects.html'
    Links to edit_project view.
    """
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


def edit_project(request, pk):
    """
    Manages de editing of an existing Project.
    On successful operation returns to projects view.

    Template for this view is 'Materials/edit_project.html'
    """
    p = Project.objects.get(pk=pk)
    form = ProjectUpload(instance=p)
    entries = p.apostila_set.all()
    data = {'doc': p, 'form': form, 'entries':entries}
    if request.method == 'POST':
        form = ProjectUpload(request.POST, instance=p)
        if form.is_valid():
            entry = form.save(commit=False)
            if 'completed' in request.POST:
                entry.completed = True
            entry.save()
            return redirect(reverse_lazy('url_projects'))
        else:
            data['form'] = form
            return render(request, 'Materials/edit_project.html', data)
    return render(request, 'Materials/edit_project.html', data)



def category(request, pk):
    """
    Manages creation and Deletion of Categoria.

    Template for this view is 'Materials/category.html'
    """
    if request.method == 'GET':
        if pk != None:
            try:
                Categoria.objects.get(pk=pk).delete()
            except:
                pass
    else:
        form = CategoryUpload(request.POST or None)
        if form.is_valid():
            form.save()

    cats = Categoria.objects.all()
    form = CategoryUpload()
    data = {'cat': cats, 'form': form}
    return render(request, 'Materials/category.html', data)


def deleteFile(pk):
    """
    Deletes a file referenced by an Apostila.

    Has no template or URL.
    """
    ap = Apostila.objects.get(pk=pk)
    try:
        os.remove(os.path.join(MEDIA_ROOT, str(ap.file)))
    except:
        pass  # silence error when no file is there


def delete(request, pk):
    """
    Deleta uma Apostila do banco de dados e qualquer arquivo referênciado por ele.

    Has no template.
    """
    doc = Apostila.objects.get(pk=pk)
    deleteFile(pk)
    doc.delete()
    return redirect('url_search')


def delete_project(request, pk):
    """
    Deletes a Project along with ALL the Apostilas related to it.
    If the Apostilas have files they are deleted as well.

    Has no template.
    """
    p = Project.objects.get(pk=pk)
    aps = p.apostila_set.all()
    for a in aps:
        # desociates project and Apostila
        a.project.remove(p)
    p.delete()
    return redirect('url_projects')
