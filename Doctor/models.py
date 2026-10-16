from django.db import models
from User.models import User 

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "Doctor")
    especialidad = models.CharField()

    def __str__(self):
        return self.user.get_full_name()