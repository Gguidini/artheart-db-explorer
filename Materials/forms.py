import django
from .models import Apostila

class ApostilaUpload(django.forms.ModelForm):

    class Meta:
        model = Apostila
        fields = ['title', 'description', 'author', 'project', 'categories', 'file', 'url']