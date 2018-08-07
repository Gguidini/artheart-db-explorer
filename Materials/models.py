"""
Models for Materials in ArtHeart environment.
There are 3 basic models:
    1) Apostila. 
    Main model. Defines a learning resource. 
    Possibly belongs to one project.
    Possibly has some category(ies)

    2) Project
    Defines a project.
    May be for a client.
    May be completed or not.

    3) Categoria
    Defines a category.
    Basically used as search filter.
"""

from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField('Nome', max_length=100)
    client = models.CharField('Cliente', max_length=100, blank=True)
    description = models.TextField('Descrição', blank=True)
    completed = models.BooleanField('Completado ?', default=False)

    def __str__(self):
        return self.name + ((' para ' + self.client) if self.client != '' else '')

class Categoria(models.Model):
    category = models.CharField('Categoria', max_length=100)

    def __str__(self):
        return self.category

class Apostila(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=100, default='Sem Título')
    description = models.TextField('Descrição', blank=True)
    author = models.CharField('Autor', max_length=50, blank=True)
    submissionDate = models.DateField(auto_now_add=True)
    project = models.ManyToManyField(Project, blank=True, null=True, help_text="Opcional. Adicione se a apostila faz parte de algum projeto.")
    categories = models.ManyToManyField(Categoria, blank=True)
    file = models.FileField(blank=True, help_text="Se estiver modificando o arquivo da Apostila, NÃO SELECIONE limpar e outro arquivo ao mesmo tempo.")
    url = models.URLField('URL', blank=True)

    def __str__(self):
        return self.title