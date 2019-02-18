from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('cyut/share483jiy0ifhvjr125/', views.cyut, name='cyut'),
]