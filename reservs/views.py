from .models import Reserv
from rest_framework import viewsets, permissions
from .serializers import ReservSerializer

class ReservViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Reserv objects
    queryset = Reserv.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = ReservSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]