# Generated by Django 2.0.7 on 2018-08-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materials', '0007_auto_20180801_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completado ?'),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='apostila',
            name='file',
            field=models.FileField(blank=True, help_text='Se estiver modificando o arquivo da Apostila, NÃO SELECIONE limpar e outro arquivo ao mesmo tempo.', upload_to='<django.db.models.fields.related.ForeignKey>', verbose_name='Arquivo'),
        ),
    ]
