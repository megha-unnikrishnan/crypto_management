
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, CryptoPriceViewSet,latest_prices
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'crypto-prices', CryptoPriceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('api/latest-prices/', latest_prices, name='latest-prices'),
]