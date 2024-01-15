from django.urls import path
from . import views

urlpatterns = [
    path('',views.policies, name='policies'),
    path('category/<int:category>/',views.category,name="category")
]