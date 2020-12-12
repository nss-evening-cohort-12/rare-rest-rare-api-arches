# Generated by Django 3.1.3 on 2020-12-12 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareserverapi', '0003_auto_20201211_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rareusers', related_query_name='rareuser', to='rareserverapi.rareusers')),
                ('post_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='rareserverapi.post')),
            ],
        ),
    ]
