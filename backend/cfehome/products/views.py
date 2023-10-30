from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .permissions import IsStaffEditor
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here.

class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)  
        
    
                                                

class ProductRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    
    
    # lookup_field = 'pk'

