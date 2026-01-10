from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
        # views.index = import from model
        # name='index' == name for this rout
    path('course/<int:course_id>', views.single_course, name='single_course'),    
]
