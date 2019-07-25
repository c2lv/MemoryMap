# Generated by Django 2.2.3 on 2019-07-25 13:48

from django.conf import settings
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_mapmodel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapmodel',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mapmodel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
