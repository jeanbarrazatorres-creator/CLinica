

from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = Doctor
        fields = ["first_name", "last_name", "email", "password", "password2"]

    def create(self, validated_data):
        password = validated_data.get("password")
        password2 = validated_data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"El password no coincide con la confirmacion "})
        
        validated_data.pop("password2")
        password = validated_data.pop("password")
        doctor = Doctor(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor 

    def validate_first_name(self, data):
        if len(data) < 3:
            raise serializers.ValidationError({"El nombre debe ser mayor a 3 caracteres"})
        return data
      
    def validate_last_name(self, data):
        if len(data) < 3:
            raise serializers.ValidationError({"El apellido debe ser mayor a 3 caracteres"})
        return data
    
    def validate_email(self, data):
        if Doctor.objects.filter(email = data).exists():
            raise serializers.ValidationError({"El email ya esta registrado"})
        return data