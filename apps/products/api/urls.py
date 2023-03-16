from django.urls import path
from apps.products.api.viewset.general_views import (
    MeasureUnitViewSet, 
    IndicatorViewSet,
    CategoryProductViewSet
)

from apps.products.api.viewset.product_viewset import ( 
    ProductListCreateAPIView, 
    ProductRetrieveUpdateDestroyAPIView
)

url_patterns = [
    path("measure_unit/", MeasureUnitViewSet.as_view(), name = "measure_unit"),
    path("indicator/", IndicatorViewSet.as_view(), name = "measure_unit"),
    path("category_product/", CategoryProductViewSet.as_view(), name = "measure_unit"),
    path("product/", ProductListCreateAPIView.as_view(), name = "product_create"),
    path("product/retrieve-update-destroy/<int:pk>", ProductRetrieveUpdateDestroyAPIView.as_view(), name = "product_retrieve-update-destroy"),
]
