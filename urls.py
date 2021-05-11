from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.showCourses, name='showCourses'),
    path('edit/',views.courseChange, name='showCourses'),
]