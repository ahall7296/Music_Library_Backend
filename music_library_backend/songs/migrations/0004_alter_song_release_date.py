# Generated by Django 4.1.7 on 2023-03-25 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_alter_song_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]