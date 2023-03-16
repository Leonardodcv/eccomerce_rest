from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.models import MeasureUnit,CategoryProduct
from apps.products.api.serializers.general_serializers import (
    MeasureUnitSerializer, 
    IndicatorSerializer, 
    CategoryProductSerializer
    )

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id = self.kwargs["pk"], state = True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Categoría registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance = self.get_object().get(), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Categoria actualizada correctamente!"}, status = status.HTTP_200_OK)
        return Response({'message':'', 'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({"message" : "Categoria eliminada correctamente!"}, status = status.HTTP_200_OK)
        return Response({'message':'', 'error':"Categoria no encontrada"}, status = status.HTTP_400_BAD_REQUEST)

    
