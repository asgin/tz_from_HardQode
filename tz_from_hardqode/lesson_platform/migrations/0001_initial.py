# Generated by Django 4.2.5 on 2023-09-21 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time_watching', models.PositiveIntegerField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_platform.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_platform.user')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_platform.user'),
        ),
        migrations.CreateModel(
            name='LessonView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_watched_in_seconds', models.PositiveIntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_platform.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_platform.user')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='product',
            field=models.ManyToManyField(related_name='lessons', to='lesson_platform.product'),
        ),
    ]