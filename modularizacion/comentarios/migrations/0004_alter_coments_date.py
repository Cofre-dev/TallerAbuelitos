# Generated by Django 5.1.3 on 2024-11-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comentarios", "0003_coments_signature"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coments",
            name="date",
            field=models.DateField(null=True),
        ),
    ]
