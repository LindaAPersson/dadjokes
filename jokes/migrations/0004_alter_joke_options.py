# Generated by Django 4.2.11 on 2024-03-07 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0003_alter_comment_options_remove_joke_title_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='joke',
            options={'ordering': ['-created_on']},
        ),
    ]