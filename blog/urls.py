from django.urls import path
from .views import PostView,PostDetailsViewsp, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
path('',PostView.as_view(),name='home'),
path('details/<int:pk>', PostDetailsViewsp.as_view(), name='detail_view'),
path('blog/new', BlogCreateView.as_view(), name='blog_create'),
path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),

]
