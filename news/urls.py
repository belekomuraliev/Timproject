from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news import views as news_views


shop_router = DefaultRouter()
shop_router.register('item', news_views.ItemViewSet)