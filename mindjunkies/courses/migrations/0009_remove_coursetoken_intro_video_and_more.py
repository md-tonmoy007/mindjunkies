# Generated by Django 5.1.7 on 2025-04-17 16:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0008_module_unique_order_per_course"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coursetoken",
            name="intro_video",
        ),
        migrations.RemoveField(
            model_name="coursetoken",
            name="motivation",
        ),
        migrations.AlterField(
            model_name="course",
            name="preview_video",
            field=cloudinary.models.CloudinaryField(default="", max_length=255),
        ),
    ]
