from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from rest_framework.renderers import JSONRenderer
from rest_framework import status, authentication, exceptions
from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(authentication.BaseAuthentication):
    user = None

    def get_user(self, request):
        
        """
        Return: 
        *user: User instance or
        *message : Error Message or
        * None : Corrup Token
        """
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)
            if user != None:
                self.user = user
                return user
        return None

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed("No se han enviado las credenciales")
        return (self.user, None)          
    """    
    El  metodo dispatch ya no es util porque no se hace la verificacion por medio del metodo mixins
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        #encuentra un token en request
        if user is not None:
            return super().dispatch(request, *args, **kwargs)
        response = Response({"error" : "No se han enviado las credenciales"},
                            status = status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
    
    def viejo_dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        #encuentra un token en request
        if user is not None:
            if type(user) == str:
                response = Response({"error" : user, "expired" : self.user_token_expired}, 
                                    status = status.HTTP_401_UNAUTHORIZED)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                return response
            if not self.user_token_expired:
                return super().dispatch(request, *args, **kwargs)
        response = Response({"error" : "No se han enviado las credenciales", 
                            "expired" : self.user_token_expired},
                            status = status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
        """
