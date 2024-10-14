from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.



class UserSignupView(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user_id":user.id})
    

class ObtainTokenPairView(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self,request,*args,**kwargs):
        user = User.objects.filter(username=request.data.get("username")).first()
        if user and user.check_password(request.data.get("password")):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error":"Invalid username or password"},status=401)
    


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)