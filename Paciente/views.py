from rest_framework.generics import CreateAPIView
from .serializers import PacienteSerializer
from .models import Paciente

class RegisterPacienteView(CreateAPIView):
    serializer_class = PacienteSerializer 
