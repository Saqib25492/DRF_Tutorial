import random
from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.query import QuerySet

# Create your models here.
User = settings.AUTH_USER_MODEL #auth.user
TAGS_MODEL_VALUES = ['cars', 'electronics', 'boats', 'movies']
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public = True)
    
    def search(self, query, user=None):
        lookup =  Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
    
class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user = None):
        return self.get_queryset().search(query, user = user)


class Product(models.Model):
    # pk = models.UUIDField(primary_key=True)
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    objects = ProductManager()
    
    
    
    @property
    def body(self):
        return self.content
    
    def is_public(self) -> bool:
        return self.public # True of False
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
    
    def __str__(self):
        return self.title
     
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "%.2f" %(float(self.price) * 0.2)
    