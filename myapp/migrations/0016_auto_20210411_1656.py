# Generated by Django 3.1.7 on 2021-04-11 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20210411_1640'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MusicalStoreInstrumentDetail',
        ),
        migrations.DeleteModel(
            name='MusicalStoreRegShow',
        ),
    ]
