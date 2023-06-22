from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'), # int stands for integer
    path('checkout/',views.checkout,name='checkout'),

    path('<int:id>',views.detail,name='detail'), # int stands for integer
    #path('checkout/',views.checkout,name='checkout'),

    #path('api/checkout-session/<int:id>/',views.create_checkout_session,name='api_checkout_session'),

]
