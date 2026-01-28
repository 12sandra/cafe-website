from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),

    path('userreg/', views.userreg, name='userreg'),
    path('userreg/ins/', views.insertuser, name='ins'),

    path('tables/', views.viewuser, name='viewuser'),

    path('edit/<int:id>/', views.edituser, name='edituser'),
    path('update/<int:id>/', views.updateuser, name='updateuser'),
    path('delete/<int:id>/', views.deleteuser, name='deleteuser'),
]
