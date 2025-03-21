from django.urls import path

from . import views
from .views import login_view, logout_view

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]