# Generated by Django 4.2.14 on 2024-07-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_jobpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="slug",
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
