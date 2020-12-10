from django.urls import path
from Newsfeed import views
urlpatterns = [

    path('',views.Newsfeed.as_view(),name="newsfeed"),
    path('/post_review',views.PostReview.as_view(),name="/post_review"),

]
