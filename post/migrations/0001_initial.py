# Generated by Django 2.2.6 on 2020-08-08 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_category',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_tag',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Category')),
                ('tag', models.ManyToManyField(to='post.Tag')),
            ],
            options={
                'db_table': 't_post',
            },
        ),
    ]
