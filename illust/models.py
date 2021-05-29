from django.db import models
from django.utils import timezone

import uuid 


# Create your models here.
class Design(models.Model):
    # テーブル名の定義
    class Meta:
        db_table = "design"

    id          = models.UUIDField( default=uuid.uuid4, primary_key=True, editable=False )

    # カラム(フィールド)の定義
    title = models.CharField(verbose_name="タイトル", max_length=100)
    date = models.DateTimeField(verbose_name="時間",default=timezone.now)
    description = models.TextField(verbose_name='説明',null=True, blank=True)

    file = models.FileField(verbose_name="ファイル", upload_to="illust/file")

    mime = models.TextField(verbose_name="MIMEタイプ",null=True, blank=True)
    thumbnail = models.ImageField(verbose_name="サムネイル", upload_to="illust/thumbnail/", null=True)

    #TIPS:サムネイル生成に失敗したデータを判定する(バッチ処理が失敗したデータを除外して生成作業をするため)
    error = models.BooleanField(verbose_name="エラー状態",default=False)



    #TODO:投稿者のユーザーIDなどのカラム(フィールド)を定義する。


    def __str__(self):
        return self.title
