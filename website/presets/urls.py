from django.urls import path

from . import views
from .views import AboutView, ChangelogView, PresetListView, PresetDetailView, PresetCreateView

app_name = 'presets'
urlpatterns = [
    path('', PresetListView.as_view(), name='index'),
    path('<int:id>/', PresetDetailView.as_view(), name='detail'),
    path('create/', PresetCreateView.as_view(), name='create'),
    path('delete/<int:preset_id>', views.delete, name='delete'),
    path('like/<int:preset_id>', views.like, name='like'),
    path('remove_like/<int:preset_id>', views.remove_like, name='dislike'),
    path('download/<int:preset_id>', views.download, name='download'),
    path('account/<int:user_id>', views.account, name='account'),
    path('update/<int:preset_id>/', views.update, name='update'),
    path('generate', views.generate_presets, name='generate'),
    path('delete-all', views.delete_presets, name='delete-all'),
    path('about', AboutView.as_view(), name='about'),
    path('changelog', ChangelogView.as_view(), name='changelog'),
]