from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginResponseSerializer, LoginSerializer, RegisterRequestSerializer, UserSerializer


class RegisterUserAPIView(APIView):
    @swagger_auto_schema(request_body=UserSerializer,
                         responses={201: RegisterRequestSerializer})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer,
                         responses={201: LoginResponseSerializer})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
