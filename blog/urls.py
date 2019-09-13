from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name="post_list"),
    path('about/',views.AboutView.as_view(),name="about"),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="post_detail"),
    path('post/create',views.CreatePostView.as_view(),name="create_post"),
    path('post/<int:pk>/update',views.UpdatePostView.as_view(),name="update_post"),
    path('post/<int:pk>/delete',views.DeletePostView.as_view(),name="delete_post"),
    path('post/<int:pk>/publish',views.publish_post,name="publish_post"),
    path('drafts',views.DraftListView.as_view(),name="draft_list"),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name="add_comment_to_post"),
    path('comment/<int:pk>/approve',views.approve_comment,name="approve_comment"),
    path('comment/<int:pk>/delete',views.delete_comment,name="delete_comment"),
]