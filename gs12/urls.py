from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('allsong/', views.SongsAPI.as_view()),
    path('platforms/<slug:pk>/', views.SongsAPI.as_view()),
    path('songs/<slug:song>/', views.SongsAPI.as_view()),
    path('artist/<slug:artist>/',views.SongsAPI.as_view()),
    path('update/<int:pk>/',views.SongsAPI.as_view()),
    path('create/',views.SongsAPI.as_view()),
    
        
    
]