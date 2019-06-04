from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('research/', views.research, name='research'),
    path('publications/', views.publications, name='publications'),
    path('teaching/', views.teaching, name='teaching'),
    path('contact/', views.contact, name='contact'),
]
