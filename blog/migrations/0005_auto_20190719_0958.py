# Generated by Django 2.2.3 on 2019-07-19 00:58

import blog.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20190716_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='mapmodel',
            options={'ordering': ('pub_date',)},
        ),
        migrations.AddField(
            model_name='mapmodel',
            name='address',
            field=models.CharField(default='장소를 지정해주세요.', max_length=200),
        ),
        migrations.AddField(
            model_name='mapmodel',
            name='like',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mapmodel',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mapmodel',
            name='image',
            field=models.ImageField(null=True, upload_to=blog.models.user_path),
        ),
    ]
