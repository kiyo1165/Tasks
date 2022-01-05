from django.shortcuts import render
from rest_framework import status, permissions, generics, viewsets
from .serializers import UserSerializer, TaskSerializer, profileSerializer, CategorySerializer
from rest_framework.response import Response
from api.models import Task, Category
from user.models import Profile
from django.contrib.auth import get_user_model


#user作成
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # 権限：誰でもアクセス可能
    permission_classes = (permissions.AllowAny, )

#user一覧取得
class ListUserView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

#ログイン中のuserを取得
#RetrieveUpdateAPIView:特定のモデルを指定できる。
class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # put methodを使用できないようにする。
    def update(self, request, *args, **kwargs):
        response = {'message': '更新はできません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    #ログイン中のuserを取得
    def get_object(self):
        return self.request.user



#ProfileのCRU
class ProfileViewSets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = profileSerializer

    #pforileの作成時にuserとの紐付けを行う。
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

    #delete methodを使用できないようにする。
    def destroy(self, request, *args, **kwargs):
        response = {'message': '削除はできません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    #patch methodを使用できないようにする。
    def partial_update(self, request, *args, **kwargs):
        response = {'message': '一部の変更はできません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # delete methodを使用できないようにする。
    def destroy(self, request, *args, **kwargs):
        response = {'message': '削除はできません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # patch methodを使用できないようにする。
    def partial_update(self, request, *args, **kwargs):
        response = {'message': '一部の変更はできません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # put methodを使用できないようにする。
    def update(self, request, *args, **kwargs):
        response = {'message': '更新はできません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


from .custompermissions import OwnerPermission
class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, OwnerPermission)

    # タスク作成時にログイン中のuserをownerにセット
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # patch methodを使用できないようにする。
    def partial_update(self, request, *args, **kwargs):
        response = {'message': '一部の変更はできません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)