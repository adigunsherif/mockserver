# Generated by Django 4.2 on 2023-04-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mocker", "0004_endpoint_full_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="endpoint",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="endpoint",
            name="endpoint_path",
            field=models.CharField(
                help_text="e.g, api/Products (without the initial and last /)",
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="server",
            name="base_path",
            field=models.CharField(
                help_text="e.g, api/Products (without the initial and last /)",
                max_length=200,
            ),
        ),
    ]
