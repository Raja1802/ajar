# Generated by Django 2.1.5 on 2019-01-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20190111_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set_1',
            name='url',
        ),
        migrations.AddField(
            model_name='set_1',
            name='image_url',
            field=models.TextField(default='', max_length=300),
        ),
    ]
