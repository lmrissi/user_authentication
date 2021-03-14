import pytest
from users.models import User

""" 
Esta função de teste cria um novo usuário utilizando o modelo User e verifica o username, 
email, se o usuário está ativo, se o usuário não é staff nem um super usuário.

A função possui um decorador que é responsável por criar uma transação no banco de dados para o teste.
Ao final do teste é realizado o rollback da transação.
"""
@pytest.mark.django_db(transaction=True)
def test_create_user():
    user = User.objects.create_user(
        username="usuario_teste", email="usuario@teste.com", password="#senhateste123"
    )

    assert user.username == "usuario_teste"
    assert user.email == "usuario@teste.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser

""" 
Esta função de teste cria um novo super usuário utilizando o modelo User e verifica o username, 
email, se o usuário está ativo, se o usuário é staff e super usuário.

Esta função de teste possui um decorador que é responsável por criar uma transação no banco de dados para o teste.
Ao final do teste é realizado o rollback da transação.
"""
@pytest.mark.django_db(transaction=True)
def test_create_superuser():
    user = User.objects.create_superuser(
        username="admin_teste", email="admin@admin.com", password="#administrador123"
    )
    assert user.username == "admin_teste"
    assert user.email == "admin@admin.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser