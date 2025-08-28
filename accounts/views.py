from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import User
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsAdminOnly
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAuthenticated, IsAdminOnly]

class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user

class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Admin can see all users, others see limited info
        if request.user.role == 'admin':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            # Non-admin users can only see their own info
            serializer = UserSerializer(request.user)
            return Response([serializer.data])


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    return Response({
        "message": "Successfully logged out",
        "detail": "Please discard your access and refresh tokens"
    }, status=status.HTTP_200_OK)