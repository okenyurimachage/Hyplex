# Generated by Django 2.1.7 on 2019-06-03 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PlexHey', '0003_auto_20190603_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('car_make1', models.CharField(max_length=1000)),
                ('car_model1', models.CharField(max_length=1000)),
                ('phonenumber', models.CharField(default=True, max_length=13, null=True)),
                ('pickupdate', models.DateField()),
                ('days', models.PositiveIntegerField()),
                ('user', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=100)),
                ('assigned', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('category', models.CharField(default='Feedback', max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('read', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='make1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=1000)),
                ('make_image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('car_price', models.PositiveIntegerField()),
                ('car_image', models.ImageField(upload_to='')),
                ('car_capacity', models.PositiveIntegerField()),
                ('model_year', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlexHey.make1')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Identification_Number', models.PositiveIntegerField()),
                ('Age', models.PositiveIntegerField()),
                ('Phone_Number', models.CharField(default=True, max_length=13, null=True)),
                ('Driving', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlexHey.make1'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlexHey.model1'),
        ),
    ]
