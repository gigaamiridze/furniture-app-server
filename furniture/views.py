from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/products',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products'
        },
        {
            'Endpoint': '/products/<int:pk>',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object'
        },
        {
            'Endpoint': '/create-product',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'Creates new product with data sent in post request'
        },
        {
            'Endpoint': '/search/<str:key>',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object or an array of products'
        },
        {
            'Endpoint': '/products/id',
            'method': 'PUT',
            'body': {'body': ''},
            'description': 'Creates an existing product with data sent in post request'
        },
        {
            'Endpoint': '/products/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting product'
        },
    ]

    return Response(routes, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all().order_by('-created_at')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': f'Product with ID {pk} not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_product(request, key):
    products = Product.objects.filter(
        Q(name__icontains=key) | Q(supplier__icontains=key) | Q(location__country__icontains=key) | Q(location__city__icontains=key)
    )

    if not products:
        return Response({'error': f'No products found for the search key "{key}".'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
