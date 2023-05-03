# Generated by Django 4.2 on 2023-04-24 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('master_table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_display', models.BooleanField(default=True)),
                ('created_at', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name_plural': 'Languages',
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='India', max_length=50)),
                ('state', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('is_display', models.BooleanField(default=True)),
                ('created_at', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_display', models.BooleanField(default=True)),
                ('created_at', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Skills',
                'db_table': 'skill',
            },
        ),
        migrations.AddField(
            model_name='designation',
            name='created_at',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='industry',
            name='created_at',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
