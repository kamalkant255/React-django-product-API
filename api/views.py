from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from .models import Product

# Create your views here.

class ProductList(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    