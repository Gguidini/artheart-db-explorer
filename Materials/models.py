from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField('Nome', max_length=100)
    client = models.CharField('Cliente', max_length=100, blank=True)

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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, help_text="Opcional. Adicione se a apostila faz parte de algum projeto.")
    categories = models.ManyToManyField(Categoria, blank=True)
    file = models.FileField(blank=True)
    url = models.URLField('URL para Documento', blank=True)

    def __str__(self):
        return self.title