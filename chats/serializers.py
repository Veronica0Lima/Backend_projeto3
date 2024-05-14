from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Messages

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# ModelSerializer do Django REST Framework para simplificar a serialização dos objetos
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'text', 'user_enviado', 'conversa']