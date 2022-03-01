from django.urls import path
from . import views

urlpatterns = [
  path('static', views.fetch_static, name='fetch_static'),
  path('db', views.fetch_db, name='fetch_db'),
]