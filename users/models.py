from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

""" 
Esta classe extende a classe de usuários padrão do Django para que seja possível realizar alterações no modelo de usuários.
A nova classe substitui o campo de ID padrão para que a pk do modelo seja definida por um uuid.
"""
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)