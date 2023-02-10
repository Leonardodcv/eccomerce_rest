from rest_framework import generics
from apps.base.api import GeneralListApiView
from apps.products.models import CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer

class IndicatorSerializerListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer

class CategoryProductSerializerListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return CategoryProduct.objects.filter(state=True)