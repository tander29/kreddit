# Generated by Django 2.2 on 2019-04-08 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subkreddit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subkreddit',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
