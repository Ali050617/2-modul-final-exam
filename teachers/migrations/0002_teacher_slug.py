# Generated by Django 5.1.5 on 2025-02-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
