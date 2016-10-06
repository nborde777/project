from django.conf.urls import include, url
from django.contrib import admin
from utm_app import views

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'edit/$',views.edit_view),
]
