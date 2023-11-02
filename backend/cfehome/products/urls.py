from django.urls import path 
from products import views


urlpatterns = [
    path('', views.ProductCreateAPIView.as_view(), name="product-list"),
    path('<int:pk>/', views.ProductRUDAPIView.as_view(), name="product-detail"),
 
] 
