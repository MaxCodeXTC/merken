# Generated by Django 2.1.8 on 2019-05-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_remove_siteconfiguration_posts_per_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemsg',
            name='content',
            field=models.TextField(default='Notification Message'),
        ),
    ]
