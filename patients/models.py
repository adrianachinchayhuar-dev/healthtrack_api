from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from doctors.models import Doctor

class Patient(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(150)],
        verbose_name="Edad"
    )
    diagnosis = models.TextField(verbose_name="Diagnóstico médico")
    
    # Relación: cada paciente tiene un doctor asignado
    doctor = models.ForeignKey(
        Doctor, 
        on_delete=models.SET_NULL,  # Si el doctor se elimina, el paciente no se pierde
        null=True, 
        blank=True,
        related_name='patients',
        verbose_name="Doctor asignado"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['id']  # Orden por ID como solicita el examen
    
    def __str__(self):
        return f"{self.name} ({self.age} años) - Dr. {self.doctor.name if self.doctor else 'Sin asignar'}"