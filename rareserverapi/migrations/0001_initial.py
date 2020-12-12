# Generated by Django 3.1.3 on 2020-12-12 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='RareUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_image_url', models.CharField(max_length=255)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('image_url', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', related_query_name='post', to='rareserverapi.category')),
                ('rareuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='rareserverapi.rareusers')),
                ('tags', models.ManyToManyField(related_name='tag_posts', related_query_name='tag_post', to='rareserverapi.Tag')),
            ],
        ),
    ]
