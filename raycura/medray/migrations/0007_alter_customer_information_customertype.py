# Generated by Django 4.1.7 on 2023-05-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medray', '0006_rename_info_customer_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_information',
            name='CustomerType',
            field=models.CharField(max_length=15),
        ),
    ]
