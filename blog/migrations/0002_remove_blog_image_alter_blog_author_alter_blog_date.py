# Generated by Django 4.2.13 on 2024-06-16 23:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
