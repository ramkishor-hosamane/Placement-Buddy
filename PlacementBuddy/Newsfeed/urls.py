from django.urls import path
from Newsfeed import views
urlpatterns = [

    path('',views.Newsfeed.as_view(),name="newsfeed"),
    path('all_questions',views.all_questions,name="all_questions"),
    path('algorithm_questions',views.algorithm_questions,name="algorithm_questions"),
    path('programming_questions',views.programming_questions,name="programming_questions"),
    path('dbms_questions',views.dbms_questions,name="dbms_questions"),
    path('cn_questions',views.cn_questions,name="cn_questions"),
    path('sw_questions',views.sw_questions,name="sw_questions"),

    path('/post_review',views.PostReview.as_view(),name="/post_review"),
    path('/fav_posts',views.fav_posts,name="/fav_posts"),

]
