from django.urls import path
from Home import views

urlpatterns = [
    path('signin',views.Signin.as_view(),name="signin"),
    path('logout',views.Signin.as_view(),name="logout"),
    
    path('', views.home,name="home"),
    path('signup',views.Signup.as_view(),name="signup"),

]
