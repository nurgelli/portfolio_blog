from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.Job_list.as_view(), name='list'),
    path('<int:pk>', views.Job_detail.as_view(), name='detail'),

]

