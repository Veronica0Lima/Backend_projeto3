from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import User
from .serializers import UserSerializer
import requests
from django.http import JsonResponse

def index(request):
    return HttpResponse("Olá mundo! Este é o app Chats do projeto WorkFlow.")

@api_view(['GET', 'POST'])
def api_users(request):
    users = User.objects.all()

    if request.method == 'POST':
        new_user_data = request.data
        print(new_user_data)
        user = User.objects.create(nome=new_user_data['nome'])
        user.save()

    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)

@api_view(['GET', 'DELETE'])
def api_user_id(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        if request.method == 'DELETE':
            user.delete()
            print(f"{user.nome} deleted")
    except User.DoesNotExist:
        raise Http404()
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)

@api_view(['GET', 'DELETE'])
def api_user_name(request, name):
    try:
        user = User.objects.get(nome=name)
        if request.method == 'DELETE':
            user.delete()
            print(f"{name} deleted")
    except User.DoesNotExist:
        raise Http404()
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)
