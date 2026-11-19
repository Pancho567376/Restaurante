"""
URL configuration for Restaurante_Polilla project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from Menu.views import ComidaDetailView, ComidaListView, ComidaCreateView, ComidaUpdateView, ComidaDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ComidaListView.as_view(), name='home'),
    path('comidas/<int:pk>/', ComidaDetailView.as_view(), name='comida_detail'),
    path('comidas/', ComidaListView.as_view(), name='comida_list'),
    path('comidas/create/', ComidaCreateView.as_view(), name='comida_create'),
    path('comidas/<int:pk>/update/', ComidaUpdateView.as_view(), name='comida_update'),
    path('comidas/<int:pk>/delete/', ComidaDeleteView.as_view(), name='comida_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
