# Generated by Django 2.2.5 on 2020-01-29 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200128_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tip',
            options={'verbose_name': 'Tip', 'verbose_name_plural': 'Tips'},
        ),
    ]