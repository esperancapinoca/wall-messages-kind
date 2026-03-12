from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall, name='wall'),
    path('', views.wall, name='wall'),
    path('like/<int:message_id>/', views.like_message, name='like_message'),
]