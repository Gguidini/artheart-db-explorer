from django.contrib import admin
from .models import Apostila, Categoria, Project

# Register your models here.
admin.site.register(Apostila)
admin.site.register(Categoria)
admin.site.register(Project)