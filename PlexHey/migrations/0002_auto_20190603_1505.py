# Generated by Django 2.1.7 on 2019-06-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlexHey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phonenumber',
            field=models.CharField(default=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Phone_Number',
            field=models.CharField(default=True, max_length=13, null=True),
        ),
    ]