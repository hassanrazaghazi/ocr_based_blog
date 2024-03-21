from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('forgot_password/', views.forgot_password, name='forgot_password'),
    # path('reset_password/', views.reset_password, name='reset_password'),
    
]
