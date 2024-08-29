from django.db import models
from django.utils import timezone

class Local(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    DIAS_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    dia = models.CharField(max_length=10, choices=DIAS_CHOICES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.dia}: {self.hora_inicio} - {self.hora_fin}'

class Instructor(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    años_experiencia = models.IntegerField()
    num_estrellas = models.IntegerField(default=5)
    descripcion = models.TextField(null=True, blank=True) 
    numero = models.CharField(max_length=15) 
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    inicio_contrato = models.DateField()
    fin_contrato = models.DateField()
    imagen = models.ImageField(upload_to='instructores/')
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

class InstructorEspecialidad(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    ruta_imagen_certificado = models.CharField(max_length=100)
    fecha_obtencion_certificado = models.DateField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.instructor.nombre} - {self.especialidad.nombre}'

# Nueva Tabla: Información Personal del Instructor
class InstructorInfoPersonal(models.Model):
    instructor = models.OneToOneField(Instructor, on_delete=models.CASCADE)
    redes_sociales = models.JSONField()
    pasatiempos = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    telefono_emergencia = models.CharField(max_length=15)
    nombre_contacto_emergencia = models.CharField(max_length=100)
    relacion_contacto_emergencia = models.CharField(max_length=50)
    email_personal = models.EmailField(max_length=100)
    nivel_educacion = models.CharField(max_length=50)
    idiomas = models.CharField(max_length=100)
    hobbies = models.TextField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    disponibilidad_viaje = models.BooleanField(default=False)
    preferencia_horario = models.CharField(max_length=50)
    alergias = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Información personal de {self.instructor.nombre}'


