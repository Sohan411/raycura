# Generated by Django 4.1.7 on 2023-05-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medray', '0014_testimonials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='description_1',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='description_2',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='name_1',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='name_2',
            field=models.CharField(max_length=40),
        ),
    ]
