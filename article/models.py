from django.db import models
from django.utils import timezone
from extensions.utils import jconverter


class Category (models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس دسته بندی ")
    status = models.BooleanField(default=False, verbose_name="انشارشود ؟ ")
    position = models.IntegerField( verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها"
        ordering=['-position']

    def __str__(self):
        return self.title




class Article (models.Model):
    title = models.CharField(max_length=200 ,verbose_name="مقاله")
    slug=models.SlugField(max_length=200 , unique=True ,verbose_name="آدرس مقاله")
    description=models.TextField(verbose_name="توضیحات")
    thumbnail=models.ImageField(upload_to="static/article/images/", blank=True ,verbose_name="عکس جاری")
    category=models.ManyToManyField(Category,verbose_name="عکس جاری")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    created=models.DateTimeField(auto_now_add=True,verbose_name="زمان ساخت")
    updated=models.DateTimeField(auto_now=True,verbose_name="به روزرسانی")
    status=models.BooleanField(default=False,verbose_name="وضعیت")

    class Meta:
        verbose_name="مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def jpublish (self):
        return jconverter(self.publish)
    jpublish.short_description = "زمان انشار "
# Create your models here.
