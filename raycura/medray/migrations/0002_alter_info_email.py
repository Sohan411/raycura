# Generated by Django 4.1.6 on 2023-02-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medray', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
