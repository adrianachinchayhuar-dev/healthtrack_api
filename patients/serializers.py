from rest_framework import serializers
from .models import Patient
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

class PatientSerializer(serializers.ModelSerializer):
    # PUNTO EXTRA ✨: Mostramos información del doctor dentro del paciente
    doctor_info = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_doctor_info(self, obj):
        """Personaliza la respuesta mostrando nombre y especialidad del doctor"""
        if obj.doctor:
            return {
                'id': obj.doctor.id,
                'name': obj.doctor.name,
                'specialty': obj.doctor.specialty
            }
        return None
    
    def validate_age(self, value):
        """Validación adicional para edad"""
        if value < 0:
            raise serializers.ValidationError("La edad no puede ser negativa")
        if value > 150:
            raise serializers.ValidationError("La edad no puede superar los 150 años")
        return value