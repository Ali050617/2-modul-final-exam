# Generated by Django 5.1.5 on 2025-02-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_remove_subject_prerequisites_delete_prerequisite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prerequisites',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
