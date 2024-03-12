# Generated by Django 4.2.11 on 2024-03-12 13:02

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0008_joke_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='slug',
            field=models.SlugField(default=builtins.id, max_length=200, unique=True),
        ),
    ]