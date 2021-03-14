from django.views.generic import TemplateView
from rest_framework.decorators import action
from rest_framework import viewsets
from users.models import User
from .serializers import DeleteUserSerializer
from django.shortcuts import redirect
from django.contrib import messages



"""
Esta view extende a classe TemplateView para renderizar a página home.
"""
class HomePageView (TemplateView):
    template_name = "home.html"

"""
Esta view extende a classe TemplateView para renderizar a página delete.
"""
class DeletePageView (TemplateView):
    template_name = "delete.html"

"""
Esta view expõe um endpoint baseado em uma função que possui um decorador action, e é utilizada para realizar o delete do usuário a partir do e-mail informado.
Diferente das outras views, esta view possui um serializador atrelado para transformar os dados do formulário em um objeto Json.
A view realiza a validação do e-mail informado antes de realizar o delete do usuário, caso o e-mail seja inválido ou o usuário não seja localizado,
uma mensagem de erro é exibida
"""
class DeleteView(viewsets.GenericViewSet):
    serializer_class = DeleteUserSerializer

    @action(methods=['POST', ], detail=False)
    def delete(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.delete()
                messages.info(request, 'Usuário deletado com sucesso')
                return redirect ("pages:home")
            except:
                messages.info(request, 'Usuário não localizado')
                return redirect ("pages:delete")
        else:
            messages.info(request, 'Digite um e-mail válido')
            return redirect ("pages:delete")

        