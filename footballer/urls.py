from django.contrib import admin
from django.urls import path
from . import views # şu anki klasörden views ı import et

appName = "footballerdashboard"

urlpatterns = [
    path('footballerdashboard/', views.footballerDashboard, name = "footballerdashboard"),
    path('addfootballer/', views.addFootballer, name = "addfootballer"),
    # path('article/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.updateFootballer, name = "updatefootballer"),
    path('delete/<int:id>', views.deleteFootballer, name = "deletefootballer"),
    # path('', views.articles, name = "articles"),
]