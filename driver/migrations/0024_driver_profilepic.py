# Generated by Django 2.2.1 on 2019-08-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0023_auto_20190719_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='profilePic',
            field=models.CharField(default='', max_length=255),
        ),
    ]
