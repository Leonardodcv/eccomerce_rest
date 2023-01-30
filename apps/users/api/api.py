from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer


@api_view(["GET", "POST"])
def user_api_view(request):
    #list
    if request.method == "GET":
        #queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)  
    #create
    elif request.method == "POST":
        #print(request.data)
        users_serializer= TestUserSerializer(data=request.data)
        #validation
        if users_serializer.is_valid():
 # al usar .save() se llama a una serie  servicios automatizados de verificacion              
            users_serializer.save()
            return Response({"message" : "Usuario creado correctamente"}, status=status.HHTP_201_CREATED)
        return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST )

"""Forma inicial pero no es la mejor forma
@api_view(["GET", "POST"])
def user_api_view(request):
    #list
    if request.method == "GET":
        #queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data)
    elif request.method == "POST":
        #print(request.data)
        users_serializer= UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors)
"""

"""
class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data)
"""

@api_view(["GET", "PUT","DELETE"])
def user_detail_api_view(request, pk=None):

    if request.method == "GET":
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    
    elif request.method == "PUT":
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    
    elif request.method == "DELETE":
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response("Eliminado")
    


