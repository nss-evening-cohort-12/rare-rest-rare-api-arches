# Generated by Django 3.1.4 on 2021-01-06 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareserverapi', '0006_auto_20210106_0148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postreactions',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='postreactions',
            old_name='reaction_id',
            new_name='reaction',
        ),
        migrations.RenameField(
            model_name='postreactions',
            old_name='user_id',
            new_name='user',
        ),
    ]
