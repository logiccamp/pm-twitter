from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    Name = serializers.CharField()
    Message = serializers.CharField()
    DatePosted = serializers.DateTimeField()



class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = ('Name', 'Message')