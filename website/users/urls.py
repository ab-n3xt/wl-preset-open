from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('create', views.create_user, name='create'),
    path('logout', views.logout_user, name='logout'),
    path('edit', views.edit_user, name='edit'),
    path('delete', views.delete_user, name='delete')
]