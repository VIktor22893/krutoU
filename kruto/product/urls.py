from . import views
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('price_list/', views.materials_list, name='materials_list'),
    path('materials/<int:pk>/', views.MaterialDetailView.as_view(), name="detail"),
    path('create/callback', views.callback_view, name="callback"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts")
] 
