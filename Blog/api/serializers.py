from .models import  Post, Comentario
from rest_framework import serializers
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_titulo(self, value):
        if not value:
            raise serializers.ValidationError("El título no puede estar vacío.")
        if len(value) > 50:
            raise serializers.ValidationError("El título no puede exceder los 50 caracteres.")
        return value


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

      def validate_contenido(self, value):
        if not value:
            raise serializers.ValidationError("El contenido del comentario no puede estar vacío.")
        return value

