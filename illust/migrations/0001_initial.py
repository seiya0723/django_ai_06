# Generated by Django 3.1.2 on 2021-05-29 06:50

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='時間')),
                ('description', models.TextField(blank=True, null=True, verbose_name='説明')),
                ('file', models.FileField(upload_to='illust/file', verbose_name='ファイル')),
                ('mime', models.TextField(blank=True, null=True, verbose_name='MIMEタイプ')),
                ('thumbnail', models.ImageField(null=True, upload_to='illust/thumbnail/', verbose_name='サムネイル')),
                ('error', models.BooleanField(default=False, verbose_name='エラー状態')),
            ],
            options={
                'db_table': 'design',
            },
        ),
    ]
