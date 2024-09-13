from django.urls import path

#todo/urls.py
from . import views
urlpatterns=[
  path('addTask',views.addTask,name="addTask")
]