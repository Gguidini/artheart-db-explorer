# Generated by Django 2.0.7 on 2018-08-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materials', '0009_auto_20180801_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apostila',
            name='project',
        ),
        migrations.AddField(
            model_name='apostila',
            name='project',
            field=models.ManyToManyField(blank=True, help_text='Opcional. Adicione se a apostila faz parte de algum projeto.', null=True, to='Materials.Project'),
        ),
    ]
