from django.urls import path
from . import views

urlpatterns = [
    path('',views.policies, name='policies'),
    path('category/<int:category_id>/',views.category,name="category")
]