from django.urls import path
from .views import RegisterPacienteView

urlpatterns = [
    path("register/paciente/", RegisterPacienteView.as_view(), name = "register_paciente")
]
