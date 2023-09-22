from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('api/v1/all/', AllLessonsView.as_view()),
    path('api/v1/product/<int:product_id>/', ProductLessonView.as_view()),
    path('api/v1/statistic_products/', StatisticView.as_view()),
]