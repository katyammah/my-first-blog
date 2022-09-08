from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('catalog/', views.catalog, name='catalog'),
    path('customer_data/', views.customer_data, name='customer_data'),
    path('ok/', views.customer_data_ok, name='customer_data_ok'),
    path('ourcontacts/', views.contacts, name = 'contacts'),
]