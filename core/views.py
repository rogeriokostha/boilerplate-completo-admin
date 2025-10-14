from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HealthCheckSerializer


class HealthCheckView(APIView):
    """Retorna o status básico da API"""

    serializer_class = HealthCheckSerializer
    permission_classes = []

    def get(self, request):
        data = {"status": "ok", "environment": "local"}
        serializer = self.serializer_class(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
