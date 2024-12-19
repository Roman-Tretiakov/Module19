# Generated by Django 5.1.4 on 2024-12-19 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_buyer_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='buyer',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
