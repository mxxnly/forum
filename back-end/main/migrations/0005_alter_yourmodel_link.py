# Generated by Django 5.0.3 on 2024-03-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_yourmodel_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourmodel',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
