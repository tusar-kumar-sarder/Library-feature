# Generated by Django 4.0.7 on 2024-11-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='educational_background',
            field=models.JSONField(blank=True, default={'Bachelors': 'BBA'}),
        ),
    ]
