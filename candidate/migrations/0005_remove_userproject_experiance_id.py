# Generated by Django 4.2 on 2023-04-27 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_alter_userexperience_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproject',
            name='experiance_id',
        ),
    ]