from django.urls import path, include
from . import views
# from views import *
urlpatterns = [
    path('', views.birortanom, name="head"),
    path('matn', views.matnnom, name="body"),
    #127.0.0.1:8000/
    #path('YOUR ROOT/', views.section, name="UNIQUENAME")
    # path('', include('myapp.urls')),
]
