# Generated by Django 4.2.7 on 2023-12-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumReleaseDate',
            field=models.DateTimeField(),
        ),
    ]
