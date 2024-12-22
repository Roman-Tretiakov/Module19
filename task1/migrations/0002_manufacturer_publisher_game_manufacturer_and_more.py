# Generated by Django 5.1.4 on 2024-12-21 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=100)),
                ('author_name', models.CharField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='manufacturer',
            field=models.ManyToManyField(to='task1.manufacturer'),
        ),
        migrations.AddField(
            model_name='news',
            name='publisher_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='task1.publisher'),
            preserve_default=False,
        ),
    ]