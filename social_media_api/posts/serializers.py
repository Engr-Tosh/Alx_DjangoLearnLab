from rest_framework import serializers
from .models import Post, Comment


# Post serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


    def validate_content(self, data):
        pass

    def validate(self, data):
        content = data.get("content")

        if len(content) <= 10 or None:
            raise serializers.ValidationError("Post is too short")
        
        return super().validate(data)
    

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]