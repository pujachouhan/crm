from django.contrib import admin
from django.urls import path
from User import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('admin/', admin.site.urls),
    path('logout/',views.logout),
]
