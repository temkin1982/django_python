from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomaAuthentication

# Create your models here.

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses' 
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['reviews_qty', 'created_at'] # מבטל את השורות האלו   
        authentication = CustomaAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        # Когда клиент отправляет данные (POST/PUT),
        # мы берём значение category_id из JSON (bundle.data)
        # и записываем его в объект модели (bundle.obj),
        # чтобы Django мог сохранить это в базу.
        bundle.obj.category_id = bundle.data['category_id']
        return bundle


    def dehydrate(self, bundle):
        # Когда мы отправляем данные клиенту (GET),
        # мы берём значение category из модели (bundle.obj.category)
        # и добавляем его в JSON-ответ под ключом category_id.
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
    
    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()