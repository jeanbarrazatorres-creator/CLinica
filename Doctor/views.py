
from rest_framework.permissions import IsAdminUser 
from rest_framework.generics import CreateAPIView 
from .serializers import DoctorSerializer 
from .models import Doctor 

class RegisterDoctorView(CreateAPIView):
    serializer_class = DoctorSerializer 
    permission_classes = [IsAdminUser]

