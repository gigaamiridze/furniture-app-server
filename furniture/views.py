from rest_framework.decorators import api_view
from rest_framework.response import Response
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
            'Endpoint': '/products/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object'
        },
        {
            'Endpoint': '/products',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'Creates new product with data sent in post request'
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

    return Response(routes)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all().order_by('-created_at')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
