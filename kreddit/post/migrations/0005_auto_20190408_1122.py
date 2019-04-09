# Generated by Django 2.2 on 2019-04-08 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subkreddit', '0001_initial'),
        ('post', '0004_post_subkreddit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subkreddit',
        ),
        migrations.AddField(
            model_name='post',
            name='subkreddit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subkreddit.SubKreddit'),
        ),
    ]
