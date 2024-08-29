from rest_framework import serializers
from collections import defaultdict
from datetime import datetime
from .models import Instructor, Cargo, Local, Especialidad, InstructorEspecialidad, Horario, InstructorInfoPersonal

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all())

    class Meta:
        model = Horario
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['instructor_nombre'] = instance.instructor.nombre
        representation['instructor_apellidos'] = instance.instructor.apellidos
        return representation
    


class InstructorSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer(read_only=True)
    local = LocalSerializer(read_only=True)
    especialidades = serializers.SerializerMethodField()
    horarios = serializers.SerializerMethodField()

    class Meta:
        model = Instructor
        fields = '__all__'

    def get_especialidades(self, obj):
        especialidades = InstructorEspecialidad.objects.filter(instructor=obj)
        # Asegúrate de incluir los campos adicionales en la serialización de especialidades
        return [{
            "nombre": e.especialidad.nombre,
            "ruta_imagen_certificado": e.ruta_imagen_certificado,
            "fecha_obtencion_certificado": e.fecha_obtencion_certificado
        } for e in especialidades]

    def get_horarios(self, obj):
        horarios = Horario.objects.filter(instructor=obj).order_by('dia', 'hora_inicio')

        horario_list = []
        for horario in horarios:
            horario_list.append({
                "dia": horario.dia,
                "hora_inicio": horario.hora_inicio.strftime('%I:%M %p'),
                "hora_fin": horario.hora_fin.strftime('%I:%M %p'),
            })
        return horario_list




class InstructorEspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorEspecialidad
        fields = '__all__'

class InstructorInfoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorInfoPersonal
        fields = '__all__'


