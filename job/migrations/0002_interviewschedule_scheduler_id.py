# Generated by Django 4.2 on 2023-04-26 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewschedule',
            name='scheduler_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='scheduler_name', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
