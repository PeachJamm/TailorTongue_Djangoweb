from django.urls import path
from . import views

urlpatterns = (
    path('', views.explore, name='explore'),#
    path('contact/',views.contact,name='contact')#
)
