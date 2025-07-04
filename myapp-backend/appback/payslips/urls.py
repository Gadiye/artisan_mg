from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PayslipViewSet

router = DefaultRouter()
router.register(r'payslips', PayslipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]