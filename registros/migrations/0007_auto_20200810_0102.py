# Generated by Django 3.0.8 on 2020-08-10 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_auto_20200809_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nota', models.CharField(max_length=200)),
                ('Comentario', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='avaliações',
            name='empresaname',
            field=models.CharField(default='Semnome', max_length=64),
        ),
        migrations.AddField(
            model_name='avaliações',
            name='username',
            field=models.CharField(default='Semnome', max_length=64),
        ),
    ]