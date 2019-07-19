# Generated by Django 2.2.3 on 2019-07-19 11:14

import blog.models
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
                ('category', models.CharField(choices=[('FOOD', '음식'), ('CAR', '자동차'), ('ETC', '기타')], default='카테고리', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mapmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('address', models.CharField(default='장소를 지정해주세요.', max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to=blog.models.user_path)),
                ('owner', models.ForeignKey(default='unknow|default 유저', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('memo', models.TextField()),
                ('owner', models.ForeignKey(default='unknow|default 유저', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memos', to='blog.Mapmodel')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
