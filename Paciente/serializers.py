from rest_framework import serializers 
from .models import Paciente 

class PacienteSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = Paciente 
        fields = ["first_name", "last_name", "email", "password", "password2"]

    def validate_first_name(self,  data):
        if len(data) < 3:
            raise serializers.ValidationError({"El nombre debe ser mayor a 3 caracteres"})
        return data

    def validate_last_name(self,  data):
        if len(data) < 3:
            raise serializers.ValidationError({"El apellido debe ser mayor a 3 caracteres"})
        return data

    def validate_email(self, data):
        if Paciente.objects.filter(email = data).exists():
            raise serializers.ValidationError({"El email ya esta registrado"})
        return data 

    def create(self, validated_data):
        password = validated_data.get("password")
        password2 = validated_data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"El password no coincide con la confirmacion"})

        validated_data.pop("password2")
        password = validated_data.pop("password")
        paciente = Paciente(**validated_data)
        paciente.set_password(password)
        paciente.save()
        return paciente 