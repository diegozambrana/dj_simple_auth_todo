from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import views, status
from .serializers import RegistrationSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
def pingPublic(request):
    return Response({"message": "ping public"})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def pingPrivate(request):
    return Response({"message": "ping private"})


class RegistrationAPIView(views.APIView):
    """
    Creates a new user.
    # Allow any user (authenticated or not) to hit this endpoint.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        # success, message = utils.check_recaptcha(request)

        # if not success:
        #     Response(data=message, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'success': True,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
