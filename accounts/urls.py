from django.urls import path
from . import views
from django.contrib import admin


 
urlpatterns = [
    path("logout/", admin.site.logout, name="logout"),
    # path('', views.home, name='home' ),
    # path("profile/<init:pk>", views.profile.as_view(), name="profile"),
    path('login/', views.login, name = 'login'),
    path("profile/", views.profile, name="profile"),
    path("save_profile/", views.save_profile, name="save_profile"),
    # path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name='signup'),
    path('admin/profile', views.admin_profile, name='admin_profile'),
    path('info', views.info_sitte, name='info_site'),
    path('save/info', views.save_info_site, name='save_info_site'),
    path('admin_name', views.admin_name, name='admin_name'),
    path('save_admin', views.save_admin, name='save_admin'),
    path('edit_admin', views.edit_admin.as_view(), name='edit_admin'),
    path('detail_admin/<int:pk>', views.detail_admin, name='detail_admins'),
    path('save_admins/<int:pk>', views.save_admins, name='save_admins'),
    path('delete_admin/<int:pk>', views.delete_admin, name='delete_admin'),
    path('about/', views.about, name='about')
    ]