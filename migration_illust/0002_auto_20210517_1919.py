# Generated by Django 2.2.6 on 2021-05-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illust', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='mime',
            field=models.TextField(blank=True, null=True, verbose_name='MIMEタイプ'),
        ),
        migrations.AddField(
            model_name='design',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='illust/thumbnail/', verbose_name='サムネイル'),
        ),
    ]
