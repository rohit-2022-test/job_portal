# Generated by Django 4.2 on 2023-05-03 12:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_alter_job_datails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='datails',
            field=ckeditor.fields.RichTextField(default='\nfghj\nfghjk\n\n\n\nfghjk\n'),
        ),
    ]
