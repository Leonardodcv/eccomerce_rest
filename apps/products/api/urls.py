from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorSerializerListAPIView, CategoryProductSerializerListAPIView
from apps.products.api.views.product_views import ProductListAPIView, ProductCreateAPIView

urlpatterns = [
    path("measure_unit/", MeasureUnitListAPIView.as_view(), name = "measure_unit"),
    path("indicator/", IndicatorSerializerListAPIView.as_view(), name = "measure_unit"),
    path("categoryproduct/", CategoryProductSerializerListAPIView.as_view(), name = "measure_unit"),
    path("product/list/", ProductListAPIView.as_view(), name = "product_list"),
    path("product/create/", ProductCreateAPIView.as_view(), name = "product_create"),
]
