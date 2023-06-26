from django.urls import path
from .import views


urlpatterns = [

    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/public/', views.PublicPosts.as_view(), name='public-posts'),
    path('posts/<int:id>/', views.PostRetriveDeleteUpdateView.as_view(),
         name='post-retrieve-update-delete'),

]
