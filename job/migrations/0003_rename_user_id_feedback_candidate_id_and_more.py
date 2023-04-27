# Generated by Django 4.2 on 2023-04-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0003_pgcourse_ugcourse_ugsubject_pgsubject'),
        ('job', '0002_interviewschedule_scheduler_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='user_id',
            new_name='candidate_id',
        ),
        migrations.RenameField(
            model_name='interviewschedule',
            old_name='user_id',
            new_name='candidate_id',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='user_id',
            new_name='creater_id',
        ),
        migrations.RenameField(
            model_name='jobapplicants',
            old_name='user_id',
            new_name='candidate_id',
        ),
        migrations.AddField(
            model_name='job',
            name='skill',
            field=models.ManyToManyField(to='master_table.skill'),
        ),
    ]
