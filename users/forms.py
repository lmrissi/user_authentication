from django.contrib.auth import forms
from .models import User

""" 
Estas classes extendem os formulários de edição e criação de usuários no admin do Django.
Não foi realizada nenhuma modificação, porém a classe está extendida para caso seja necessária alguma alteração seja mais fácil aplicá-la.
"""
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User