from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('board/', views.board, name='board'),   
    path('test/', views.test, name='test'),
    path('Insert_data/', views.Insert_data, name='Insert_data'),
    
]