from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import Product
from .serializers import ProductSerializer

class ProductPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    page_query_param = 'offset'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination