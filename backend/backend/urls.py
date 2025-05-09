"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views as api_views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')), # URLs pour la connexion (login)
    path('api/articles/', api_views.ArticleListCreateView.as_view(), name='article-list-create'),
    path('api/articles/<int:pk>/', api_views.ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
    path('api/register/', api_views.register_user, name="register"),
    path("api/ping", api_views.ping, name="ping"),
    path("api/connexion/", api_views.connexion, name="connexion")
]