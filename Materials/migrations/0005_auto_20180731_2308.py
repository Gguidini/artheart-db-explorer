# Generated by Django 2.0.7 on 2018-08-01 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Materials', '0004_auto_20180731_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apostila',
            name='file',
            field=models.FileField(blank=True, help_text='Se estiver modificando o arquivo da Apostila, NÂO SELECIONE limpar e outro arquivo ao mesmo tempo.', upload_to=''),
        ),
        migrations.AlterField(
            model_name='apostila',
            name='project',
            field=models.ForeignKey(blank=True, help_text='Opcional. Adicione se a apostila faz parte de algum projeto.', null=True, on_delete=django.db.models.deletion.CASCADE, to='Materials.Project'),
        ),
    ]
