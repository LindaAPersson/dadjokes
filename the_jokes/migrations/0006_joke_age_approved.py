# Generated by Django 4.2.11 on 2024-03-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_jokes', '0005_rating_joke_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='age_approved',
            field=models.BooleanField(default=False),
        ),
    ]
