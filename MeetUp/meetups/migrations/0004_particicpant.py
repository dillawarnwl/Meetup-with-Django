# Generated by Django 4.1.7 on 2023-04-01 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_location_meetup_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Particicpant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
