# Generated by Django 4.2.11 on 2024-03-21 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('the_jokes', '0004_joke_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_creator', to=settings.AUTH_USER_MODEL)),
                ('joke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_joke', to='the_jokes.joke')),
            ],
        ),
        migrations.AddField(
            model_name='joke',
            name='ratings',
            field=models.ManyToManyField(related_name='rated_jokes', through='the_jokes.Rating', to=settings.AUTH_USER_MODEL),
        ),
    ]