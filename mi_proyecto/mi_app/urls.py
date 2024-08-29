from django.urls import path
from . import views
from .views import (
    InstructorListCreateView, InstructorRetrieveUpdateDestroyView,
    CargoListCreateView, CargoRetrieveUpdateDestroyView,
    LocalListCreateView, LocalRetrieveUpdateDestroyView,
    EspecialidadListCreateView, EspecialidadRetrieveUpdateDestroyView,
    InstructorEspecialidadListCreateView, InstructorEspecialidadRetrieveUpdateDestroyView,
    HorarioListCreateView, HorarioRetrieveUpdateDestroyView, InstructorInfoPersonalRetrieveView
)

urlpatterns = [
    path('instructores/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('instructores/<int:pk>/', InstructorRetrieveUpdateDestroyView.as_view(), name='instructor-detail'),
    path('cargos/', CargoListCreateView.as_view(), name='cargo-list-create'),
    path('cargos/<int:pk>/', CargoRetrieveUpdateDestroyView.as_view(), name='cargo-detail'),
    path('locales/', LocalListCreateView.as_view(), name='local-list-create'),
    path('locales/<int:pk>/', LocalRetrieveUpdateDestroyView.as_view(), name='local-detail'),
    path('especialidades/', EspecialidadListCreateView.as_view(), name='especialidad-list-create'),
    path('especialidades/<int:pk>/', EspecialidadRetrieveUpdateDestroyView.as_view(), name='especialidad-detail'),
    path('instructor-especialidad/', InstructorEspecialidadListCreateView.as_view(), name='instructor-especialidad-list-create'),
    path('instructor-especialidad/<int:pk>/', InstructorEspecialidadRetrieveUpdateDestroyView.as_view(), name='instructor-especialidad-detail'),
    path('horarios/', HorarioListCreateView.as_view(), name='horario-list-create'),
    path('horarios/<int:pk>/', HorarioRetrieveUpdateDestroyView.as_view(), name='horario-detail'),
    path('instructor-info-personal/<int:pk>/', InstructorInfoPersonalRetrieveView.as_view(), name='instructor-info-personal-detail'),


    # Vistas
    path('instructoreslist/', views.instructors_list_view, name='instructores-list'),
    path('instructornew/', views.nuevo_instructor_view, name='nuevo-instructor'),
]
