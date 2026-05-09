from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    specialty = models.CharField(max_length=200, verbose_name="Especialidad médica")
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="Correo electrónico")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ['id']  # Orden por ID como solicita el examen
    
    def __str__(self):
        return f"Dr(a). {self.name} - {self.specialty}"