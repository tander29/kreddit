# Generated by Django 2.2 on 2019-04-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subkreddit', '0001_initial'),
        ('post', '0003_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subkreddit',
            field=models.ManyToManyField(to='subkreddit.SubKreddit'),
        ),
    ]
