# Generated by Django 2.2 on 2019-04-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190317_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='allow_comments',
            field=models.BooleanField(default=True),
        ),
    ]
