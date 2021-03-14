from rest_framework import serializers
from users.models import User


""" 
Este serializador transforma os dados recebidos do formulário em um objeto Json.
A classe ainda possui um método delete que realiza a exclusão do usuário no banco de dados utilizando a ORM do Django.
"""
class DeleteUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('email',)

    def delete (self):
        user = User.objects.get(email=self.validated_data['email'])
        user.delete()