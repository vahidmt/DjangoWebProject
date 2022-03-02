from rest_framework import serializers
from .models import blogg
 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogg
        fields = ['id', 'title', 'text_blog']