# Generated by Django 3.1.2 on 2021-05-22 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illust', '0002_auto_20210517_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='error',
            field=models.BooleanField(default=False, verbose_name='エラー状態'),
        ),
    ]
