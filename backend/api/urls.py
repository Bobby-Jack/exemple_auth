from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', views.ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
    path('register/', views.register_user, name="register")
]

