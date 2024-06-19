from django.urls import path, include
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    CategoryView, CategoryListView, LikeView, AddCommentView, DeleteCommentView, UnLikeView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:categorys>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('unlike/<int:pk>', UnLikeView, name='unlike_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment_delete/<int:pk>', DeleteCommentView.as_view(), name='delete_comment'),
]
