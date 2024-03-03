# Generated by Django 5.0.2 on 2024-03-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                related_name="posts", through="tags.TagPostSet", to="tags.tag"
            ),
        ),
    ]