from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('share125vjr/', views.cyut, name='cyut'),
    path('version/', views.version, name='version'),
    path('connection/', views.connection, name='connection'),
    path('computer/', views.computer, name='computer')
]
