# Generated by Django 2.1.7 on 2019-06-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlexHey', '0008_booking_pickupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pickupdate',
            field=models.DateTimeField(null=True),
        ),
    ]
