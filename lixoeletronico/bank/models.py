from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class LocaisDescarte(models.Model):
    # codigo = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    nome_local = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    celular = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    site = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome_local