# Generated by Django 3.2.5 on 2021-07-27 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rc_desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SignInEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att_abs_type', models.CharField(choices=[('1REG', '1REG'), ('6ADL', '6ADL'), ('ANLL', 'ANLL')], default='1REG', max_length=4)),
                ('location', models.CharField(choices=[('offi', 'office'), ('home', 'home'), ('fiel', 'field')], default='offi', max_length=4, verbose_name='Work Location For Day')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Sign In Date')),
                ('time', models.TimeField(default=datetime.time(7, 0), verbose_name='Sign In Time')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Notes:')),
            ],
        ),
        migrations.CreateModel(
            name='SignOutEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Sign Out Date')),
                ('time', models.TimeField(default=datetime.time(7, 0), verbose_name='Sign Out Time')),
                ('lunch_start', models.TimeField(default=datetime.time(12, 0), verbose_name='Lunch Start')),
                ('lunch_end', models.TimeField(default=datetime.time(12, 30), verbose_name='Lunch End')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Notes:')),
            ],
        ),
    ]
