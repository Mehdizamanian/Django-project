from django.contrib import admin
from .models import Article ,Category





class CategoryAdmin (admin.ModelAdmin):
    list_display = ["position","title","slug","status",]
    list_filter = (["status"])
    search_fields = ("title", "description")
    ordering = ["-status"]

admin.site.register(Category,CategoryAdmin)






class ArticleAdmin (admin.ModelAdmin):
    list_display = ["title","jpublish","status","category_to_str"]
    list_filter = (["status"])
    search_fields = ("title","description")
    ordering = ["-status"]

    def category_to_str(self,obj):
        self.description = 'ددسته'
        return ", ".join([category .title for category in obj.category.all()])

    category_to_str.short_description = "دسته بندی  "

admin.site.register(Article,ArticleAdmin)


# Register your models here.
