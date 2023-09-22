from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *
from .serializer import *

def AllLessonViewLogic(self, request):
    products_accessed = ProductAccess.objects.filter(user=request.user)
    products = Product.objects.filter(id__in=products_accessed.values('product'))
    answer = {}
    data = []
    for product in products:
        product_data = {
            'product': ProductSerializer(product).data,
            'lessons': LessonSerializer(Lesson.objects.filter(product=product), many=True, context={'request': self.request}).data
        }
        data.append(product_data)
    return JsonResponse(data, safe=False)

def ProductLessonViewLogic(self, request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if ProductAccess.objects.filter(user=request.user, product=product).first():
        lessons = Lesson.objects.filter(product=product)
        data = {}
        for lesson in lessons:
            data[lesson.id] = LessonSerializer(lesson, context={'request': self.request}).data
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'You have not access to this product'})