from django.urls import path
from . import views

urlpatterns = [
    path('', views.testing, name='testing'),
    path('accounts/login/', views.third_party_login, name='third_part_login')
]
