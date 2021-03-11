from django.contrib import admin
from django.urls import path
from . import views # şu anki klasörden views ı import et

appName = "teamdashboard"

urlpatterns = [
    path('teamdashboard/', views.teamDashboard, name = "teamdashboard"),
    path('addteam/', views.addTeam, name = "addteam"),
    path('teamdetail/<int:id>', views.teamDetail, name = "teamdetail"),
    path('updateteam/<int:id>', views.updateTeam, name = "updateteam"),
    path('deleteteam/<int:id>', views.deleteTeam, name = "deleteteam"),
    # path('', views.articles, name = "articles"),
]