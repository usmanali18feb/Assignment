from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ListAllProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReadUpdateDeleteProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListByName(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Product.objects.filter(name=name)

class ListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)

class ListByAvailability(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        availability = self.kwargs['availability']
        return Product.objects.filter(availability=availability)
