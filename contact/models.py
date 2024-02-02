from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(("Nome"), max_length=50)
    last_name = models.CharField(("Sobrenome"), max_length=50, blank=True)
    phone = models.CharField(("Telefone"), max_length=50)
    email = models.EmailField(("Email"), max_length=254, blank=True)
    created_date= models.DateTimeField(("Data Registro"),default=timezone.now)
    description = models.TextField(("Comentarios"),blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'