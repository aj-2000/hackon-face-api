

from django.urls import path
from .views import home, compare_faces, add_user

urlpatterns = [
    path('', home),
    path('cmp_faces', compare_faces),
    path('add_user', add_user)      
]      
