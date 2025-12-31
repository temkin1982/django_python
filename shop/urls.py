from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
        # /admin/ login/?next=/admin/  
]
