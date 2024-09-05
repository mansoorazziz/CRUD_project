from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='test'),
    path('contact_us/', views.c_form, name='contact'),
    path('saveitem/', views.save_item, name='contact_u'),
    path('newform/', views.new_form, name='contact_new'),

    # Registration, login and logout Urls 
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
]
