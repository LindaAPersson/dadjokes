# Generated by Django 4.2.11 on 2024-03-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_jokes', '0002_alter_joke_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='joke',
            options={'ordering': ['created_on']},
        ),
    ]
