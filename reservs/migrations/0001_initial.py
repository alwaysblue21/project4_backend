# Generated by Django 4.2.5 on 2023-09-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('number_of_customers', models.CharField(max_length=200)),
            ],
        ),
    ]
