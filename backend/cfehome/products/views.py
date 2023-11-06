from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.mixins import StaffEditorMixin, UserQuerySetMixin
from products.paginations import MyPaginatin, MyLimitPagination

# Create your views here.

class ProductCreateAPIView(UserQuerySetMixin, ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    pagination_class = MyLimitPagination
    
    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content = content)  
 
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     print(request)
    #     print(request.user)
    #     return qs.filter(user=request.user)       
    
                                                

class ProductRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    
    
    # lookup_field = 'pk'

