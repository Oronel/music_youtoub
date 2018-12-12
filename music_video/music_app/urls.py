from . import views
from django.urls import path

app_name='music_app'

urlpatterns = [
path('home/', views.home, name='home'),
]