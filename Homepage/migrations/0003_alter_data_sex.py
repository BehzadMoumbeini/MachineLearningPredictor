# Generated by Django 3.2.16 on 2023-01-22 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0002_alter_data_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True),
        ),
    ]