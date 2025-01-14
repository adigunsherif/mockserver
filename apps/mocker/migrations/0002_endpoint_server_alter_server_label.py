# Generated by Django 4.2 on 2023-04-04 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mocker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="endpoint",
            name="server",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="endpoints",
                to="mocker.server",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="server",
            name="label",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Server Name/Label"
            ),
        ),
    ]