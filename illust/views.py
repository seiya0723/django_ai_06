from django.shortcuts import render,redirect
from django.views import View

#ビュークラスに継承させることで、認証状態をチェックする
from django.contrib.auth.mixins import LoginRequiredMixin




from .models import Design
from .forms import DesignForm

import magic

ALLOWED_MIME    = [ "image/vnd.adobe.photoshop","application/pdf","application/postscript" ]

class illustView(View):

    def get(self, request, *args, **kwargs):

        #Designクラスを使用し、DBへアクセス、データ全件閲覧


        button1     = "Prev"
        data        = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        category    = "カテゴリ−１"
        category2   = "カテゴリ−2"
        category3   = "カテゴリ−3"

        context = {
                   "button1":button1,
                   "data":data,
                   "category1":category,
                   "category2": category2,
                   "category3": category3,

                   }

        return render(request,"illust/index.html",context)


index   = illustView.as_view()



#LoginRequiredMixinでログイン状態をチェック、認証状態にあればアクセスを許可する。
#class uploadView(LoginRequiredMixin,View):
class uploadView(View):

    def get(self, request, *args, **kwargs):

        designs = Design.objects.all()
        context = {
            "designs": designs,

        }
        return render(request, "illust/upload.html",context)

    def post(self, request, *args, **kwargs):


        if "file" not in request.FILES:
            return redirect("illust:index")

        mime_type = magic.from_buffer(request.FILES["file"].read(1024), mime=True)
        print(mime_type)


        copied          = request.POST.copy()
        copied["mime"]  = mime_type

        form = DesignForm(copied, request.FILES)

        if form.is_valid():
            print("バリデーションOK ")
            if mime_type in ALLOWED_MIME:
                result  = form.save()
            else:
                print("このファイルは許可されていません")
                return redirect("illust:upload")
        else:
            print("バリデーションNG")
            return redirect("illust:upload")



        """
        design = Design.objects.filter(id=result.id).first()


        from django.conf import settings
        path = Design.thumbnail.field.upload_to
        thumbnail_path = path + str(design.id) + ".png"
        full_path = settings.MEDIA_ROOT + "/" + thumbnail_path

        # フォトショップの場合
        if design.mime == "image/vnd.adobe.photoshop":
            from psd_tools import PSDImage
            image = PSDImage.open(settings.MEDIA_ROOT + "/" + str(design.file))
            image.composite().save(full_path)

        # イラストレーターの場合
        elif design.mime == "application/postscript":
            from PIL import Image
            image = Image.open(settings.MEDIA_ROOT + "/" + str(design.file))
            image.save(full_path)
        else:
            return redirect("illust:upload")

        design.thumbnail = thumbnail_path
        design.save()

        """


        return redirect("illust:upload")


upload  = uploadView.as_view()
