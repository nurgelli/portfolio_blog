from django.urls import path
from . import views


app_name = 'tech'

urlpatterns = [
    path('', views.Tech_list.as_view(), name='list'),
    path('<int:id>/', views.Tech_detail.as_view(), name='detail'),
    path('create/', views.Create_tech.as_view(), name='create'),
    path('<int:id>/update/', views.Update_tech.as_view(), name='update'),
    path('<int:id>/delete/', views.Delete_tech.as_view(), name='delete'),
    
]
