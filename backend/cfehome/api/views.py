from django.forms.models import model_to_dict
from products.models import Product
from products.serializer import ProductSerializer
from rest_framework.response import Response            
from rest_framework.decorators import api_view, throttle_classes    
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle  
                                                                  


# Create your views here.

@api_view(["GET", "POST"])
@throttle_classes([AnonRateThrottle, UserRateThrottle]) 
def api_home(request, *args, **kwargs):
    """
        DRF API VIEW
    """
    if request.method == 'GET':
        model_data = Product.objects.all() 
        data = ProductSerializer(model_data, many = True).data                                                                                   
        return Response(data)
    
    if request.method == 'POST':

        serializer = ProductSerializer(data = request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()            
            return Response({'msg':'Data Created Succesfully'})
        return Response(serializer.errors)                                                        