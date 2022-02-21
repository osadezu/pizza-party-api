from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'password',)


class UserSerializer(UserCreateSerializer):
    # member = serializers.ReadOnlyField()

    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'password', 'member')
        depth = 2
