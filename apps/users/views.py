from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.authentication_mixins import Authentication
from apps.users.api.serializers import ( 
    CustomTokenObtainPairSerializer, CustomUserSerializer)

from apps.users.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    "token" : login_serializer.validated_data.get("access"),
                    "refresh-token" : login_serializer.validated_data.get("refresh"),
                    "user" : user_serializer.data,
                    "message" : "Inicio de Sesion Exitoso"
                }, status = status.HTTP_200_OK)
            return Response({"error" : "Contraseña o nombre de usuario incorrectos"}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"error" : "Contraseña o nombre de usuario incorrectos"}, status = status.HTTP_400_BAD_REQUEST)
    
class Logout(GenericAPIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id = request.data.get("user", ""))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({"message" : "Sesion cerrada correctamente"}, status = status.HTTP_200_OK)
        return Response({"error" : "No existe este usuario"}, status = status.HTTP_400_BAD_REQUEST)




































#las siguientes clases no se usaran para nada seran sustituidas por lo que 
#este ensima
# Create your views here.
class UserToken11(Authentication, APIView):
    """
    validacion del token
    """
    def get(self, request, *args, **kwargs):
        try:
            user_token,_= Token.objects.get_or_create(user = self.user)
                #user = UserTokenSerializer().Meta.model.objects.filter(
                 #       username = username).first()
            user = UserTokenSerializer(self.user)
            return Response({
                "token": user_token.key,
                "user" : user.data
            })
        except:
            return Response({
                "error" : "Credenciales enviadas incorrectas."
            }, status = status.HTTP_400_BAD_REQUEST)


class Login11(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        # envia al serializador el usuario y la contraseña
        login_serializer = self.serializer_class(data = request.data, context = {"request":request})
        if login_serializer.is_valid():
            # login serializer retorna el usuario en validated_data
            user = login_serializer.validated_data["user"]
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        "token" : token.key,
                        "user" : user_serializer.data,
                        "message" : "Inicio de sesion exitoso"
                    }, status = status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get("_auth_user_id")):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        "token" : token.key,
                        "user" : user_serializer.data,
                        "message" : "Inicio de sesion exitoso"
                    }, status = status.HTTP_201_CREATED)
                    """token.delete()
                    return Response({
                        "error":"Ya se ha iniciado sesion con ese usuario"
                    }, status= status.HTTP_409_CONFLICT)
                    """
            else:
                return Response({"error" : "Este usuario no puede iniciar sesion"}, 
                status= status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error" : "Nombre de usuario o contrasena incorrectos"},
            status=status.HTTP_400_BAD_REQUEST)
        return Response({"mensaje":"Hola desde reponse"}, status = status.HTTP_200_OK)

class Logout11(APIView):

    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get("token")
            print(token)
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get("_auth_user_id")):
                            session.delete()
                token.delete()

                session_message = "Sesiones de usuario eliminadas."
                token_message = "Token eliminado"
                return Response ({"token_message" : token_message, "session_message" : session_message},
                                status = status.HTTP_200_OK)
            return Response({"error" : "No se ha encontrado un usuario con estas credenciales"},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error" : "No se ha encontrado token en la peticion"},
            status=status.HTTP_409_CONFLICT)
    """
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get("token")
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now)
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get("_auth_user_id")):
                            session.delete()
                
                token.delete()

                session_message = "Sesiones de usuario eliminados."
                token_message = "Token eliminado."
                
                return Response({"token_message" : token_message, "session_message" : session_message},
                                status = status.HTTP_200_OK)
            
            return Response({"error" : "No se ha encontrdo un usuario con estas credenciales"},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error" : "No se ha encontrado token en la peticion"},
                                status=status.HTTP_409_CONFLICT)
"""