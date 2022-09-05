# Generated by Django 4.1 on 2022-08-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_brand_model_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="first_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="mobile_number",
            new_name="password",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="address",
            new_name="repeat_password",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_name",
        ),
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(default=1, max_length=75),
            preserve_default=False,
        ),
    ]
