from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('follow/<str:user_name>/', views.add_follow_view, name="follower_page"),
    path('unfollow/<str:user_name>/', views.add_unfollow_view, name="unfollower_page"),
    path('profile/<str:user_name>', views.profile_view, name="profilepage"),
     

]