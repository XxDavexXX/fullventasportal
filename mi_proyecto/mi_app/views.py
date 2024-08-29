from rest_framework import generics
from .models import Instructor, Cargo, Local, Especialidad, InstructorEspecialidad, Horario, InstructorInfoPersonal
from .serializers import InstructorSerializer, HorarioSerializer, CargoSerializer, LocalSerializer, EspecialidadSerializer, InstructorEspecialidadSerializer, InstructorInfoPersonalSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import InstructorFilter, HorarioFilter, CargoFilter, LocalFilter, EspecialidadFilter, InstructorEspecialidadFilter
from django.shortcuts import render

def instructors_list_view(request):
    return render(request, 'instructores/instructores_list.html')

def nuevo_instructor_view(request):
    return render(request, 'instructores/instructores_new.html')

class InstructorListCreateView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InstructorFilter

class InstructorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CargoListCreateView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CargoFilter

class CargoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class LocalListCreateView(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LocalFilter

class LocalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class EspecialidadListCreateView(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EspecialidadFilter

class EspecialidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class InstructorEspecialidadListCreateView(generics.ListCreateAPIView):
    queryset = InstructorEspecialidad.objects.all()
    serializer_class = InstructorEspecialidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InstructorEspecialidadFilter

class InstructorEspecialidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstructorEspecialidad.objects.all()
    serializer_class = InstructorEspecialidadSerializer

class HorarioListCreateView(generics.ListCreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HorarioFilter

class HorarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class InstructorInfoPersonalRetrieveView(generics.RetrieveAPIView):
    queryset = InstructorInfoPersonal.objects.all()
    serializer_class = InstructorInfoPersonalSerializer
