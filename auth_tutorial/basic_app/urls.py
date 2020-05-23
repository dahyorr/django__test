from django.urls import path
from . import views

app_name = "basic_app"
urlpatterns =[
    path('', views.index, name='Home'),
    path('register/', views.register, name='Register'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    # path('special/', views.special, name='Special'),
]
