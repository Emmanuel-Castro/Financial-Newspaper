# Generated by Django 5.1 on 2024-08-22 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('edited', models.BooleanField()),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag')),
            ],
        ),
    ]
