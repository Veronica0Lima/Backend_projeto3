from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404  
from rest_framework.response import Response
from django.http import Http404, HttpResponseForbidden, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .serializers import UserSerializer
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

def index(request):
    return HttpResponse("Olá mundo! Este é o app Chats do projeto WorkFlow.")

@api_view(['GET', 'POST'])
def api_users(request):
    users = User.objects.all()

    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response(status=204)

    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)

@api_view(['GET', 'DELETE'])
def api_user_id(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'DELETE':
        user.delete()
        print(f"{user.username} deleted")
        return Response(status=204)
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)

@api_view(['GET', 'DELETE'])
def api_user_name(request, name):
    user = get_object_or_404(User, username=name)
    if request.method == 'DELETE':
        user.delete()
        print(f"{name} deleted")
        return Response(status=204)
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)

@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()
