from django.urls import path, include
from rest_framework import routers
from .views import *

#ModelViewSets用のエンドポイント
router = routers.DefaultRouter()
router.register('category', CategoryViewSets)
router.register('tasks', TaskViewSets)
router.register('profile', ProfileViewSets)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateUserView.as_view(), name="create"),
    path('users/', ListUserView.as_view(), name="users"),
    path('loginuser/', LoginUserView.as_view(), name="loginuser"),
]



