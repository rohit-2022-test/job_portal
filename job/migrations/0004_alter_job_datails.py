# Generated by Django 4.2 on 2023-05-03 11:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_user_id_feedback_candidate_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='datails',
            field=ckeditor.fields.RichTextField(default='My default value'),
        ),
    ]