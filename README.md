# Desafio técnico Resh Cyber Defense
Candidato: Leonardo de Melo Rissi

# Como rodar o projeto

- No terminal, execute o comando:
```
docker-compose up --build
```

- Posteriormente execute as migrations:
```
docker-compose exec web python manage.py migrate
```

- Para rodar os testes:
```
docker-compose exec web pytest
```

- Para criar um superuser para acessar a interface de admin:
```
docker-compose exec web python manage.py createsuperuser
```

- Outra opção para executar os comandos acessando o container:
```
docker-compose exec web bash
```

E a partir daí rodar os comandos normalmente, sem acrescentar `docker-compose exec web` na frente.

Por fim, acesse o site neste link: [http://localhost:8000/](http://localhost:8000/)

Qualquer dúvida estou à disposição.

# Sobre o projeto

A implementação do projeto foi baseada na biblioteca django-allauth, que oferece uma aplicação que permite a autenticação de usuários.

O django-allauth expõe diversos endpoints com views que podem ser extendidas e modificadas com a finalidade de adequá-las ao seu projeto.

Neste projeto foram utilizadas as views de login, logout, signup e gerenciamento de e-mails do django-allauth.

Os templates destas views foram personalizados e adequados as necessidades do projeto.

Além das views extendidas do django-allauth, foi implementada uma view própria que realiza a exclusão do usuário a partir do e-mail informado.

As views de gerenciamento de e-mails, exclusão de usuários e logout só podem ser visualizadas por usuários que estão autenticados no sistema.

O modelo de usuários padrão do django foi extendido para que fosse possível realizar personalizações. 

No projeto a primary key do modelo User foi alterada para que fosse gerada a partir de um uuid.

Para realização de testes foi utilizada a biblioteca pytest, que possibilita uma integraçao com o django através do pytest-django.

Foram realizados testes para as views, modelos e admin, verificando os possíveis casos de uso do sistema.

Os formulários que realizam requisições POST possuem o token CSRF.

A Secret Key foi ocultada utilizando o python-decouple, para que este dado não esteja disponível para o público.