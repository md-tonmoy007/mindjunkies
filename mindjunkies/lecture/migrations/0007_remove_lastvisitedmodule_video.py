# Generated by Django 5.2 on 2025-04-25 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0006_lastvisitedmodule_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastvisitedmodule',
            name='video',
        ),
    ]
