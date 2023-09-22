from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import *
from .serializer import *
from .logic import *

class AllLessonsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return AllLessonViewLogic(self, request)
    
class ProductLessonView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, product_id):
        return ProductLessonViewLogic(self, request, product_id)

class StatisticView(generics.ListAPIView):
    serializer_class = StatisticSerializer
    queryset = Product.objects.all()