# Generated by Django 4.1.3 on 2025-03-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(default=' ', max_length=1000),
        ),
    ]
