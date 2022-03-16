from django.urls import path, include
from . import views
urlpatterns = [
    path('new_blog', views.blog, name='save_blog'),
    path('', views.home.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    path('weblog', views.weblog_admin.as_view(), name='weblog'),
    path('save_blog/<int:pk>', views.save_blog, name='save_blog'),
    path('delete_blog/<int:pk>', views.delete_blog, name='delete_blog'),
    path('detail_admin/<int:pk>', views.detail_admin, name='detail_admin'),
    path('search/', views.search, name="search"),
    path("test", views.test, name="test")
    # path('send_email/', views.send_email, name='send_email')
    ]
