# Generated by Django 3.1 on 2020-08-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_box_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='food'),
            preserve_default=False,
        ),
    ]