from django.urls import path
from .views import login, register, logOut, postContent, myPage, updateContent, deleteContent

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logOut, name="Logout"),
    path('postcontent/', postContent, name='postcontent'),
    path('mypage/', myPage, name='mypage'),
    path('update/<int:id>', updateContent, name='update'),
    path('delete/<int:id>', deleteContent, name='delete'),
]

