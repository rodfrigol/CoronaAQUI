# Generated by Django 3.0.8 on 2020-08-10 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_auto_20200809_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='Comentario',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='Nota',
        ),
        migrations.AddField(
            model_name='avaliações',
            name='empresa_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='avaliações',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
