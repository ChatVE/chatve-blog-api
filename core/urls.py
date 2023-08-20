from django.urls import path
from .import views


urlpatterns = [
    path('api/posts', views.PostList.as_view()),
    path('api/posts/<str:pk>', views.PostDetail.as_view()),
]