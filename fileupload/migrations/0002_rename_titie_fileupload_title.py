# Generated by Django 4.2 on 2023-04-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='titie',
            new_name='title',
        ),
    ]
