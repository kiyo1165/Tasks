from rest_framework import serializers
from models import Task, Category
from user.models import User, Profile
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5,
                'required': True,
            }
        }

    #ハッシュ化したパスワードを保存
    # create_userはBaseUserManagerを引用
    def create(self, **validated_data):
        user = get_user_model().create_user(**validated_data)
        return user


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user_profile', 'img')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'item')

class TaskSerializer(serializers.ModelSerializer):

    #リレーションをもつfieldの参照を、参照先の任意のfieldで表示させる。
    category_item = serializers.ReadOnlyField(source='category.item', read_only=True)
    owner_name = serializers.ReadOnlyField(source='owner.name', read_only=True)
    responsible_name = serializers.ReadOnlyField(source='responsible.name', read_only=True)

    #choice fieldの値を取得 ※source='get_choices変数名の小文字_display'
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    #表示フォーマットの変更
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = (
            'id','task','description','criteria',
            'status','status_name','category','category_item',
            'estimate','responsible','responsible_name',
            'owner','owner_name',
            'created_at','updated_at',
        )
        extra_kwargs = {
            'owner': {
                'read_only': True
            }
        }
