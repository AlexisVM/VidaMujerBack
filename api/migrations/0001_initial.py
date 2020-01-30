# Generated by Django 3.0.1 on 2020-01-30 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_pago', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('imagen', models.ImageField(upload_to='conceptos')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='paquetes')),
                ('costo', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField()),
                ('imagen', models.ImageField(upload_to='tips')),
            ],
            options={
                'verbose_name': 'Tip',
                'verbose_name_plural': 'Tips',
            },
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('imagen', models.ImageField(upload_to='paquetes')),
                ('consulta', models.BooleanField()),
                ('costo', models.PositiveSmallIntegerField()),
                ('usuarios', models.ManyToManyField(through='api.Compra', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='paquete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Paquete'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
