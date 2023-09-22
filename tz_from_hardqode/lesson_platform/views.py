from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import *
from .serializer import *
from django.http import JsonResponse

class AllLessonsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
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
    
class ProductLessonView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        if ProductAccess.objects.filter(user=request.user, product=product).first():
            lessons = Lesson.objects.filter(product=product)
            data = {}
            for lesson in lessons:
                data[lesson.id] = LessonSerializer(lesson, context={'request': self.request}).data
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'You have not access to this product'})

class StatisticView(generics.ListAPIView):
    serializer_class = StatisticSerializer
    queryset = Product.objects.all()