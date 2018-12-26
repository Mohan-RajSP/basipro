from django.contrib import admin
from django.urls import path, include
from basiapp import urls,views

app_name = "basiapp"

urlpatterns = [
    path('',views.userform,name="FORMFILL_app"),
    path('login/',views.user_login, name="user_login"),
    path('logout/',views.user_logout, name="user_logout")
]
