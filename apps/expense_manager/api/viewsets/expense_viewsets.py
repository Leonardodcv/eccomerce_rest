from django.db.models import Q

from rest_framework import status, viewsets
from rest_framework.decoratores import action
from rest_framework.response import Response

from apps.products.models import Product
from apps.expense_manager.api.serializers.general_serializer import *
from apps.expense_manager.api.serializers.expense_serializers import *
from apps.expense_manager.models import (
    Supplier, Voucher, PaymentType
)

class ExpenseViewSet(viewsets.GenericViewSet):
    serializers_class = ExpenseSerializer

    @action(methods=["get"], detail = False)
    def search_supplier(self, request):
        ruc_or_business_name = request.query_params.get("ruc_or_business_name", "")
        supplier = Supplier.objects.filter(
            Q(ruc__iexact = ruc_or_business_name) |
            Q(business_name__iexact = ruc_or_business_name)
        ).first()
        if supplier:
            supplier_serializer = SupplierSerializer(supplier)
            return Response(supplier_serializer.data, status = status.HTTP_200_OK)
        return Response({
            "message":"No se ha encontrado un provedor"
        }, status = status.HTTP_400_BAD_REQUEST)
    
    @action(methods=["post"], detail=False)
    def new_suplier(self, request):
        data_supplier = request.data
        data_supplier = SupplierRegisterSerializer(data = data_supplier)
        if data_supplier.is_valid():
            data_supplier = data_supplier.save()
            return Response({
                "message":"Proveedor registrado correctamente",
                "supplier":data_supplier
            }, status = status.HTTP_201_CREATED)
        return Response({
            "error":data_supplier.errors
            },status = status.HTTP_400_BAD_REQUEST)
    
    @action(methods = ["get"], detaill =False)
    def get_vouchers(self, request):
        data = Voucher.objects.filter(state = True).order_by("id")
        data = VoucherSerializer(data, many = True).data
        return Response(data)

    @action(methods = ["get"], detaill =False)
    def get_payment_type(self, request):
        data = PaymentType.objects.filter(state = True).order_by("id")
        data = PaymentTypeSerializer(data, many = True).data
        return Response(data)
    
    @action(methods = ["get"], detaill =False)
    def get_products(self, request):
        data = Product.objects.filter(state = True).order_by("id")
        data = ProductSerializer(data, many = True).data
        return Response(data)
    
    def create(self, request):
        pass