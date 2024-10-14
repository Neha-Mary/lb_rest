# employees/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignupView, ObtainTokenPairView, EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('signup/', UserSignupView.as_view({'post': 'create'}), name='signup'),
    path('login/', ObtainTokenPairView.as_view({'post': 'create'}), name='login'),
    path('', include(router.urls)),
]
