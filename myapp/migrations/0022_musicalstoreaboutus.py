# Generated by Django 3.1.7 on 2021-04-15 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20210414_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalStoreAboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('desc1', models.TextField(null=True)),
                ('desc2', models.TextField(null=True)),
                ('desc3', models.TextField(null=True)),
                ('desc4', models.TextField(null=True)),
                ('img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
