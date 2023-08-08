# Generated by Django 4.1.6 on 2023-02-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=15)),
                ('Last_Name', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Contact', models.CharField(max_length=12, unique=True)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]