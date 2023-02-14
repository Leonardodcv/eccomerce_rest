from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):
    
    # TODO : Define fields here
    description = models.CharField("Descripcion", max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):

    # TODO : Define fields here
    description = models.CharField("Descripcion", max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria de producto"
        verbose_name_plural = "Categorias de productos"

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    # TODO : Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name = "Indicador de descuento")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de oferta"

    def __str__(self):
        return f"Oferta de la categoria {self.category_product} : {self.descount_value}%"

class Product(BaseModel):

    # TODO : Define fields here
    name = models.CharField("Nombre de Producto",max_length=150, unique =True, blank=False, null=False)
    description = models.TextField("Descripcion del producto", blank=True, null=True)
    image = models.ImageField("Imagen del producto", upload_to="products/", blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name="Unidad de medida", null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name="Categoria del producto", null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    
