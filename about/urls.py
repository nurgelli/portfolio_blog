from django.urls import path
from . import views

app_name = 'about'


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_list, name='list'),
    path('projects/<int:id>/', views.project_detail, name='detail'),
    path('projects/create/', views.project_create, name='create'),
    path('projects/<int:id>/update', views.project_update, name='update'),
    path('projects/<int:id>/delete/', views.project_delete, name='delete')

]
