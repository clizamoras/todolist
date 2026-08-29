from django.urls import path
from .views import tasklist,taskdetail,taskcreate,taskupdate,taskdelete,logins,RegisterPage,logout_user


urlpatterns=[
    path('login/',logins.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',tasklist.as_view(),name='tasklist'),
    path('tasks/<int:pk>/',taskdetail.as_view(),name='taskdetail'),
    path('task-create/',taskcreate.as_view(),name='task-create'),
    path('taskupdate/<int:pk>/',taskupdate.as_view(),name='taskupdate'),
    path('taskdelete/<int:pk>/',taskdelete.as_view(),name='taskdelete'),
]