from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('customer_data/', views.customer_data, name='customer_data'),
    path('ok/', views.customer_data_ok, name='customer_data_ok'),
    path('our_contacts/', views.contacts, name='contacts'),
    path('registration', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('password_reset', views.MyPasswordResetView.as_view(), name='password_reset1'),
    path('accounts/login/', views.registration, name='registration')
]
