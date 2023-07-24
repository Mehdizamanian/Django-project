
from django.urls import path , include
from .views import index


app_name="article"

urlpatterns = [

    path ('', index ,name='home'),
    # path('/<int:id>', indexdetail, name="indexdetail"),
     # path('api', api ,name="api")


]