# Generated by Django 4.2 on 2023-04-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mocker", "0002_endpoint_server_alter_server_label"),
    ]

    operations = [
        migrations.AlterField(
            model_name="server",
            name="base_path",
            field=models.CharField(help_text="e.g, api/Products", max_length=200),
        ),
    ]
