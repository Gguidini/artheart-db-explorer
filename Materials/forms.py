import django
from .models import Apostila, Project, Categoria

class ApostilaUpload(django.forms.ModelForm):
    """ Form for Apostila model (see models.py) """
    class Meta:
        model = Apostila
        fields = ['title', 'description', 'author', 'project', 'categories', 'file', 'url']

class ProjectUpload(django.forms.ModelForm):
    """ Form for Project model (see models.py) """
    class Meta:
        model = Project
        fields = ['name', 'client', 'description']

class CategoryUpload(django.forms.ModelForm):
    """ Form for Categoria model (see models.py) """
    class Meta:
        model = Categoria
        fields = ['category']