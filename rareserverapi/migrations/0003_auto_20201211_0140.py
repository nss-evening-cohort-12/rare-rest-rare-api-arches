# Generated by Django 3.1.3 on 2020-12-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareserverapi', '0002_category_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
    ]