# Generated by Django 3.1.7 on 2021-04-17 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_musicalstorereg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicalstorereg',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]
