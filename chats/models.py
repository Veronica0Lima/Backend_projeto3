from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username
    
class Conversa(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_conversas', null=True)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_conversas', null=True)


class Messages(models.Model):
    text = models.CharField(max_length=100)
    user_enviado = models.ForeignKey(User, on_delete=models.CASCADE)    # ID do Usuário
    conversa = models.ForeignKey(Conversa, on_delete=models.CASCADE)    # ID da Conversa