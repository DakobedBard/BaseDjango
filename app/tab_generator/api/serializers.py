from rest_framework import serializers
#from tab_generator.models import GuitarTab
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



# class TabSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GuitarTab
#         fields = ['title','body','image', 'bucket','youtube_link']