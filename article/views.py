from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Article , Category


def index (request):
    context={
        "article":Article.objects.filter(status=True) ,
        "category":Category.objects.filter(status=True)
    }
    return render(request,"article/index.html",context)


# def indexdetail (request,id):
#     context={"article":Article.objects.get(id=id)}
#     return render(request,"article/article.html",context)


# def api (request):
#     return JsonResponse({"fuclk":"you"})
# # برای پاسخ جیسانی باید یک دیکشنری تعریف شود

# Create your views here.
