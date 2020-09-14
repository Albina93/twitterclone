from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('follow/<str:user_name>/', views.AddFollowView.as_view(), name="follower_page"),
    path('unfollow/<str:user_name>/', views.AddUnfollowView.as_view(), name="unfollower_page"),
    path('profile/<str:user_name>', views.ProfileView.as_view(), name="profilepage"),
     

]