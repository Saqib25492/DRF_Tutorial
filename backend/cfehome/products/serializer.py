from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from .validators import validata_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source = 'user', read_only = True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk',
        )
    
    
    # email = serializers.EmailField(write_only = True)
    title = serializers.CharField(validators = [unique_product_title, validata_title_no_hello])
    # name = serializers.CharField(source = 'title', read_only=True)
    class Meta:
        model = Product
        fields = ['owner',
                  'url',
                  'pk',
                  'title',
                  'content',
                  'price',
                ]
    
    # Overriding the create method but this is used when you are add some arbitary field to serializer other wise its not recommended
    # def create(self, validated_data):
    #     #email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     #print(email, obj)
    #     return obj    

    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already exists in our database")
        return value
    
    # def get_edit_url(self, obj):
    #     # return f"api/products/{obj.pk}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
        
    #     return reverse("product-detail", kwargs = {"pk":obj.pk}, request = request)
    
    def get_my_discount(self, obj):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()