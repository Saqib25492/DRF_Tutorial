from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet, ProductGenericApiViewSet

router = DefaultRouter()
router.register('products-abc', ProductGenericApiViewSet, basename='products')

# print(router.urls)
urlpatterns = router.urls