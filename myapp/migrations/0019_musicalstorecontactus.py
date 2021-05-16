# Generated by Django 3.1.7 on 2021-04-15 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20210411_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalStoreContactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('number', models.TextField(null=True)),
                ('email', models.IntegerField(null=True)),
                ('created', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField(null=True)),
            ],
        ),
    ]
