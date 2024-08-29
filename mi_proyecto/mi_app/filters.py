import django_filters
from django_filters import rest_framework as filters
from .models import Instructor, Cargo, Local, Especialidad, InstructorEspecialidad, Horario


class InstructorFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    apellidos = django_filters.CharFilter(lookup_expr='icontains')
    años_experiencia = django_filters.NumberFilter()
    num_estrellas = django_filters.NumberFilter()
    genero = django_filters.ChoiceFilter(choices=Instructor.GENERO_CHOICES)
    local = django_filters.ModelChoiceFilter(queryset=Local.objects.all())
    cargo = django_filters.ModelChoiceFilter(queryset=Cargo.objects.all())
    especialidades = django_filters.ModelChoiceFilter(queryset=Especialidad.objects.all(), field_name='instructorespecialidad__especialidad')
    inicio_contrato = django_filters.DateFilter(field_name='inicio_contrato')
    fin_contrato = django_filters.DateFilter(field_name='fin_contrato')
    estado = django_filters.BooleanFilter()
    fecha_creacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_creacion')
    fecha_actualizacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_actualizacion')
    dia = django_filters.CharFilter(field_name='horario__dia', lookup_expr='exact')
    hora_inicio = django_filters.TimeFilter(field_name='horario__hora_inicio', lookup_expr='exact')
    hora_fin = django_filters.TimeFilter(field_name='horario__hora_fin', lookup_expr='exact')

    class Meta:
        model = Instructor
        fields = [
            'nombre',
            'apellidos',
            'años_experiencia',
            'num_estrellas',
            'genero',
            'local',
            'cargo',
            'especialidades',
            'inicio_contrato',
            'fin_contrato',
            'estado',
            'fecha_creacion',
            'fecha_actualizacion',
            'dia',
            'hora_inicio',
            'hora_fin',
        ]

class CargoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    estado = django_filters.BooleanFilter()
    fecha_creacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_creacion')
    fecha_actualizacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_actualizacion')

    class Meta:
        model = Cargo
        fields = ['nombre', 'estado', 'fecha_creacion', 'fecha_actualizacion']

class LocalFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    estado = django_filters.BooleanFilter()
    fecha_creacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_creacion')
    fecha_actualizacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_actualizacion')

    class Meta:
        model = Local
        fields = ['nombre', 'estado', 'fecha_creacion', 'fecha_actualizacion']

class EspecialidadFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    estado = django_filters.BooleanFilter()
    fecha_creacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_creacion')
    fecha_actualizacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_actualizacion')

    class Meta:
        model = Especialidad
        fields = ['nombre', 'estado', 'fecha_creacion', 'fecha_actualizacion']
        

class InstructorEspecialidadFilter(django_filters.FilterSet):
    instructor = django_filters.ModelChoiceFilter(queryset=Instructor.objects.all())
    especialidad = django_filters.ModelChoiceFilter(queryset=Especialidad.objects.all())
    estado = django_filters.BooleanFilter()
    fecha_creacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_creacion')
    fecha_actualizacion = filters.IsoDateTimeFromToRangeFilter(field_name='fecha_actualizacion')

    class Meta:
        model = InstructorEspecialidad
        fields = ['instructor', 'especialidad', 'estado', 'fecha_creacion', 'fecha_actualizacion']


class HorarioFilter(django_filters.FilterSet):
    dia = django_filters.CharFilter(field_name='dia', lookup_expr='icontains')
    hora_inicio = django_filters.TimeFilter(field_name='hora_inicio', lookup_expr='exact')
    hora_fin = django_filters.TimeFilter(field_name='hora_fin', lookup_expr='exact')

    class Meta:
        model = Horario
        fields = ['dia', 'hora_inicio', 'hora_fin', 'instructor']



