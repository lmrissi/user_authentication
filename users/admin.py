from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm
from .models import User

""" 
Esta nova classe extende a classe que registra os formulários do admin do modelo de usuários.
Nenhuma modificação foi realizada em relação ao padrão, contudo a classe está extendida para facilitar possíveis melhorias no admin de usuários.
"""
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User