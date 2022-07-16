

from django.urls import path
from .views import home, compare_faces

urlpatterns = [
    path('', home),
    path('api', compare_faces)      
]