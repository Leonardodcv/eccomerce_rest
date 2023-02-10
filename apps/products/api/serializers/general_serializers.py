from rest_framework import serializers
from apps.products.models import MeasureUnit, CategoryProduct, Indicator

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ("state","created_date","modified_data", "deleted_date")

class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ("state","created_date","modified_data", "deleted_date")

class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicator
        exclude = ("state","created_date","modified_data", "deleted_date")