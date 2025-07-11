from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnifiedInventoryViewSet as InventoryViewSet

router = DefaultRouter()
router.register(r'', InventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
