from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login, name="login"),
    path("home",views.index,name="home"),
    path("logout",views.logout,name="logout")
  
   

    
]
        