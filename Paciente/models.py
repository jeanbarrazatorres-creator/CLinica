from django.db import models
from User.models import User 

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "paciente")

    def __str__(self):
        return self.user.get_full_name()