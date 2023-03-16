from rest_framework.routers import DefaultRouter
from rest_framework import routers


from apps.products.api.viewset.general_views import *
from apps.products.api.viewset.product_viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"measure-unit", MeasureUnitViewSet, basename="measure_unit")
router.register(r"indicators", IndicatorViewSet, basename="indicators")
router.register(r"category-products", CategoryProductViewSet, basename="category_products")

urlpatterns = router.urls

"""
router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = router.urls
"""