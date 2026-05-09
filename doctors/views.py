from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    """
    GET: Listar todos los doctores
    POST: Crear un nuevo doctor
    """
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'specialty', 'email']
    ordering_fields = ['id', 'name', 'specialty']

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtener un doctor específico
    PUT/PATCH: Actualizar un doctor
    DELETE: Eliminar un doctor
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer