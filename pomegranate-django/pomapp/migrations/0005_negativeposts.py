# Generated by Django 5.1.3 on 2024-11-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pomapp", "0004_alter_post_profile_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="NegativePosts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_id", models.IntegerField()),
            ],
        ),
    ]
