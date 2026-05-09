from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    """
    GET: Listar todos los pacientes
    POST: Crear un nuevo paciente
    Búsqueda: GET /patients/?search=termino (busca en nombre y diagnóstico)
    """
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'diagnosis']  # 🔍 Búsqueda por nombre o diagnóstico
    ordering_fields = ['id', 'name', 'age', 'created_at']

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtener un paciente específico
    PUT/PATCH: Actualizar un paciente
    DELETE: Eliminar un paciente
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer