# Generated by Django 2.1.7 on 2019-06-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlexHey', '0012_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
