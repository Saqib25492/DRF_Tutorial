from rest_framework import viewsets, mixins
from .models import Product
from .serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #by default
    
    
class ProductGenericApiViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #by default
    
    
# product_list_view = ProductGenericApiViewSet.as_view({'get':'list'})
# product_detail_view = ProductGenericApiViewSet.as_view({'get':'retrieve'})