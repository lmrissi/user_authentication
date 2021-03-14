from django.test import SimpleTestCase
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from users.admin import UserAdmin
from users.models import User
from users.forms import UserChangeForm, UserCreationForm

"""  
Esta classe realiza testes na classe UserAdmin, os métodos testam se o admin de usuários foi registrado corretamente,
se o modelo da classe UserAdmin é o modelo User, se a classe UserAdmin herda da classe auth_admin.UserAdmin e se os 
formulários do UserAdmin são UserChangeForm e UserCreationForm.
"""
class UserAdminTestCase(SimpleTestCase):

    def test_registrado(self):
        self.assertTrue(
            User in admin.site._registry,
            msg="O admin de usuários não foi registrado corretamente"
        )

    def test_model_correto(self):
        self.assertEqual(
            UserAdmin.model,
            User,
            msg="Configure o admin de usuários com o modelo correto de usuários (User)"
        )

    def test_heranca(self):
        self.assertTrue(
            issubclass(UserAdmin, auth_admin.UserAdmin),
            msg="O admin dos usuários deve ser uma subclasse da classe auth_admin.UserAdminn"
        )

    def test_change_form(self):
        self.assertEqual(
            UserAdmin.form,
            UserChangeForm,
            msg="Configure o formulário de edição do admin de usuários com o formulário correto (UserChangeForm)"
        )

    def test_creation_form(self):
        self.assertEqual(
            UserAdmin.add_form,
            UserCreationForm,
            msg="Configure o formulário de criação do admin de usuários com o formulário correto (UserCreationForm)"
        )