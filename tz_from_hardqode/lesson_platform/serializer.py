from rest_framework import serializers
from .models import *
from django.db.models import Sum

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()
    time_watched = serializers.SerializerMethodField()
    class Meta:
        model = Lesson
        fields = ('name', 'link', 'is_viewed', 'time_watched')

    def get_is_viewed(self, model):
        request = self.context.get('request')
        if LessonView.objects.get(user=request.user, lesson=model).watched:
            return 'Viewed'
        else:
            return 'Not viewed'
    
    def get_time_watched(self, model):
        request = self.context.get('request')
        lesson_view = LessonView.objects.filter(user=request.user, lesson=model).first()
        if lesson_view:
            return lesson_view.time_watching
        else:
            return 0
        
class ProductLessonSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()
    time_watched = serializers.SerializerMethodField()
    last_watched = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('name', 'time_watched', 'is_viewed', 'last_watched')

    def get_is_viewed(self, model):
        request = self.context.get('request')
        if LessonView.objects.get(user=request.user, lesson=model).watched:
            return 'Viewed'
        else:
            return 'Not viewed'
        
    def get_time_watched(self, model):
        request = self.context.get('request')
        lesson_view = LessonView.objects.filter(user=request.user, lesson=model).first()
        if lesson_view:
            return lesson_view.time_watching
        else:
            return 0
    
    def get_last_watched(self, model):
        request = self.context.get('request')
        lesson_view = LessonView.objects.filter(user=request.user, lesson=model).first()
        if lesson_view:
            return lesson_view.last_watched
        else:
            return None
    
class StatisticSerializer(serializers.ModelSerializer):
    number_of_lessons_watched = serializers.SerializerMethodField()
    all_time_watched = serializers.SerializerMethodField()
    number_of_students = serializers.SerializerMethodField()
    percent_buy_product = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('name', 'number_of_lessons_watched', 'all_time_watched', 'number_of_students', 'percent_buy_product')

    def get_number_of_lessons_watched(self, model):
        lessons = Lesson.objects.filter(product=model)
        self.watched = LessonView.objects.filter(lesson__in=lessons)
        return self.watched.exclude(watched=False).count()
    
    def get_all_time_watched(self, model):
        return self.watched.aggregate(Sum('time_watching'))
    
    def get_number_of_students(self, model):
        self.count_stundets_in_product = ProductAccess.objects.filter(product=model).count()
        return self.count_stundets_in_product
    
    def get_percent_buy_product(self, model):
        return self.count_stundets_in_product / User.objects.all().count()