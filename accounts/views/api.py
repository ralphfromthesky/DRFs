from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth.models import User


from ..models.models import UserProfile
from ..serializers.serializers import RegisterSerializer, LoginSerializer, AssignRoleSerializer, UserListSerializer
from ..permissions.permissions import IsAdminRole


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        UserProfile.objects.create(user=user, role='viewer')
        
        return Response({
            "message" : "User registered successfully."
        },status=status.HTTP_201_CREATED)
        
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"message": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Login successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })
        
        
class AssignRoleView(APIView):
    permission_classes = [IsAdminRole]
    
    def post(self, request):
        serializer = AssignRoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = serializer.validated_data['user_id']
        role = serializer.validated_data['role']
        
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return Response(
                {"message": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        user_profile.role = role
        user_profile.save()
        
        return Response(
            {"message": f"Role updated successfully to '{role}'."},
            status=status.HTTP_200_OK
        )
        
class UserListView(APIView):
    permission_classes = [IsAdminRole]
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)