from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('saudacao/<str:nome>/', views.saudacao, name='saudacao'),
    path('produto/<int:id_produto>/', views.produtos, name="produto")
]