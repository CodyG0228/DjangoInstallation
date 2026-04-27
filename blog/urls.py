from django.urls import path
from . import views 


#CREATE A LIST OF URL PATTERNS THAT WHEN A URL IS VISITED, IS TIED TO A FUNCTION CALL

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]