# Generated by Django 4.1.7 on 2023-03-25 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musaaj', '0004_alter_audiomodel_id_alter_photomodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiomodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='photomodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
