from django.shortcuts import render
from django.shortcuts import HttpResponse





from rest_framework import viewsets, permissions
from .models import Organization, CryptoPrice
from .serializers import OrganizationSerializer, CryptoPriceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name'] 

class CryptoPricePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CryptoPriceViewSet(viewsets.ModelViewSet):
    queryset = CryptoPrice.objects.all()
    serializer_class = CryptoPriceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    pagination_class = CryptoPricePagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'price', 'timestamp']  # Fields you want to allow ordering
    ordering = ['id']  # Default ordering


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Max
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def latest_prices(request):
    """View to show the latest prices for all organizations"""
    from .models import Organization, CryptoPrice
    
    result = {}
    orgs = Organization.objects.all()
    
    for org in orgs:
        org_data = {"name": org.name, "prices": {}}
        
        # Get the latest BTC price
        btc_price = CryptoPrice.objects.filter(
            org=org,
            symbol="BTC"
        ).order_by('-timestamp').first()
        
        # Get the latest ETH price
        eth_price = CryptoPrice.objects.filter(
            org=org,
            symbol="ETH"
        ).order_by('-timestamp').first()
        
        if btc_price:
            org_data["prices"]["BTC"] = {
                "price": float(btc_price.price),
                "updated_at": btc_price.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            
        if eth_price:
            org_data["prices"]["ETH"] = {
                "price": float(eth_price.price),
                "updated_at": eth_price.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            
        result[str(org.id)] = org_data
    
    return Response(result)

# Create your views here.
