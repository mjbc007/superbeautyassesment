from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import EquipoSerializer
from .models import Equipo

class EquipoViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Equipo.objects.all()
        serializer = EquipoSerializer(queryset, many=True)
        return Response(serializer.data)