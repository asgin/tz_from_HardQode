# Generated by Django 4.2.5 on 2023-09-21 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_platform', '0003_lessonview_watched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonview',
            name='time_watched_in_seconds',
        ),
    ]