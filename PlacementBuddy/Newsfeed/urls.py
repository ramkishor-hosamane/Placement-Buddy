from django.urls import path
from Newsfeed import views
urlpatterns = [

    path('',views.Newsfeed.as_view(),name="newsfeed"),

]
