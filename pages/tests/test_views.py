import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed
from users.models import User
import uuid
from django.test import Client

"""
As funções abaixo possuem um decorador que as transformam em fixtures.
Estas funções podem ser acessadas pelas funções de teste por meio de argumentos 
e possuem função de organização para o código ou para executar uma ação.
"""

@pytest.fixture
def home_response(client):
    return client.get(reverse("pages:home"))

@pytest.fixture
def login_response(client):
    return client.get(reverse("account_login"))

@pytest.fixture
def logout_response(client):
    return client.get(reverse("account_logout"))

@pytest.fixture
def signup_response(client):
    return client.get(reverse("account_signup"))

@pytest.fixture
def delete_response(client):
    return client.get(reverse("pages:delete"))

@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        kwargs['email'] = 'e-mail_teste@teste.com.br'
        kwargs['password'] = '#senhateste1234'
        if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user


""" 
Esta classe testa a view Home e verifica se o endpoint, o template e o status code retornado pela view estão corretos ao realizar uma requisição HTTP GET.
"""

class TestHomePageView:
    def test_reverse_resolve(self):
        assert reverse("pages:home") == "/"
        assert resolve("/").view_name == "pages:home"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "home.html")

""" 
Esta classe testa a view de Login e verifica se o endpoint, o template e o status code retornado pela view estão corretos ao realizar uma requisição HTTP GET.
Além disso, o teste test_login_view cria um usuário a partir de uma fixture e faz o teste de login deste usuário.
"""
class TestLoginView:
    def test_reverse_resolve(self):
        assert reverse("account_login") == "/accounts/login/"
        assert resolve("/accounts/login/").view_name == "account_login"

    @pytest.mark.django_db(transaction=True)
    def test_status_code(self, login_response):
        assert login_response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_template(self, login_response):
        assertTemplateUsed(login_response, "account/login.html")

    @pytest.mark.django_db
    def test_login_view(client, create_user):
        user = create_user()
        url = reverse('account_login')
        c = Client()
        c.login(
            email=user.email, password=user.password
        )
        response = c.get(url)
        assert response.status_code == 200

""" 
Esta classe testa a view de Logout e verifica se o endpoint, o template e o status code retornado pela view estão corretos ao realizar uma requisição HTTP GET.
Além disso, o teste test_logout_view cria um usuário a partir de uma fixture, faz o login deste usuário e posteriormente verifica o logout.
"""
class TestLogoutView:
    def test_reverse_resolve(self):
        assert reverse("account_logout") == "/accounts/logout/"
        assert resolve("/accounts/logout/").view_name == "account_logout"

    def test_status_code(self, logout_response):
        assert logout_response.status_code == 302

    @pytest.mark.django_db
    def test_logout_view(client, create_user):
        user = create_user()
        url = reverse('account_logout')
        c = Client()
        c.login(
            email=user.email, password=user.password
        )
        c.logout()
        response = c.get(url)
        assert response.status_code == 302
""" 
Esta classe testa a view de Signup e verifica se o endpoint, o template e o status code retornado pela view estão corretos ao realizar uma requisição HTTP GET.
Além disso, o teste test_signup_view realiza o teste de criação de um usuário através desta view realizando uma requisição HTTP POST.
"""
class TestSignupView:
    def test_reverse_resolve(self):
        assert reverse("account_signup") == "/accounts/signup/"
        assert resolve("/accounts/signup/").view_name == "account_signup"

    @pytest.mark.django_db(transaction=True)
    def test_status_code(self, signup_response):
        assert signup_response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_template(self, signup_response):
        assertTemplateUsed(signup_response, "account/signup.html")

    @pytest.mark.django_db
    def test_signup_view(client):
        url = reverse('account_signup')
        c = Client()
        response = c.post(url, {'email': 'teste123@teste.com.br', 'password1': '#senhateste123'})
        assert response.status_code == 200

""" 
Esta classe testa a view de Delete e verifica se o endpoint, o template e o status code retornado pela view estão corretos ao realizar uma requisição HTTP GET.
Além disso, o teste test_delete_user_view realiza o teste de deletar um usuário através desta view realizando uma requisição HTTP POST.
Os cenários onde um e-mail informado é inválido ou o usuário não encontrado também foram testados.
"""
class TestDeleteView:
    def test_reverse_resolve(self):
        assert reverse("pages:delete") == "/delete/"
        assert resolve("/delete/").view_name == "pages:delete"

    @pytest.mark.django_db(transaction=True)
    def test_status_code(self, delete_response):
        assert delete_response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_template(self, delete_response):
        assertTemplateUsed(delete_response, "delete.html")

    @pytest.mark.django_db
    def test_delete_user_view(client, create_user):
        user = create_user()
        url = reverse('pages:delete_user')
        c = Client()
        c.login(
            email=user.email, password=user.password
        )
        response = c.post(url, {'email': 'e-mail_teste@teste.com.br'})
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_delete_user_view_usuario_nao_localizado(client, create_user):
        user = create_user()
        url = reverse('pages:delete_user')
        c = Client()
        c.login(
            email=user.email, password=user.password
        )
        response = c.post(url, {'email': 'outro_email@teste.com.br'})
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_delete_user_view_email_invalido(client, create_user):
        user = create_user()
        url = reverse('pages:delete_user')
        c = Client()
        c.login(
            email=user.email, password=user.password
        )
        response = c.post(url, {'email': 'email@invalido'})
        assert response.status_code == 302
