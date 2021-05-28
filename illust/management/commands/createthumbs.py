from django.core.management.base import BaseCommand

from django.conf import settings
from ...models import Design

from psd_tools import PSDImage
from PIL import Image

from pdf2image import convert_from_path
#↑pip install pdf2imageでインストール


import time

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        #パス指定
        path = Design.thumbnail.field.upload_to

        #サムネイル生成処理をループ化
        while True:

            #ここで該当データの抽出
            #サムネイルがNULLもしくはblank状態になっている場合、なおかつerrorfalseの場合
            designs = Design.objects.filter(error=False,thumbnail="")
            print(designs)

            #ここで該当データのサムネイル生成作業
            for design in designs:

                thumbnail_path = path + str(design.id) + ".png"
                full_path = settings.MEDIA_ROOT + "/" + thumbnail_path

                if design.mime == "image/vnd.adobe.photoshop":
                    image = PSDImage.open(settings.MEDIA_ROOT + "/" + str(design.file))
                    image.composite().save(full_path)
                    design.thumbnail = thumbnail_path

                elif design.mime == "application/postscript":
                    image = Image.open(settings.MEDIA_ROOT + "/" + str(design.file))
                    image.save(full_path)
                    design.thumbnail = thumbnail_path

                elif design.mime == "application/pdf":
                    images = convert_from_path(settings.MEDIA_ROOT + "/" + str(design.file))
                    images[0].save(full_path)
                    design.thumbnail = thumbnail_path

                else:
                    #生成できないものにはエラーフラグ
                    design.error = True

                #サムネイルのサイズを調整する処理
                if not design.error:
                    image           = Image.open(settings.MEDIA_ROOT + "/" + str(design.thumbnail))
                    image_resize    = image.resize((500,500))
                    image_resize.save(full_path)
                    print("リサイズ")

                design.save()

            time.sleep(1)

