from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(("Categoria"), max_length=50)
   
    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(("Nome"), max_length=50, help_text='help text')
    last_name = models.CharField(("Sobrenome"), max_length=50, blank=True)
    phone = models.CharField(("Telefone"), max_length=50)
    email = models.EmailField(("Email"), max_length=254, blank=True)
    created_date= models.DateTimeField(("Data Registro"),default=timezone.now)
    description = models.TextField(("Comentarios"),blank=True)
    show=models.BooleanField(default=True)
    picture = models.ImageField(("Foto"),blank=True,upload_to='pictures/%Y/%m/%d')
    category = models.ForeignKey(Category,verbose_name= ("Categoria"), 
                                 on_delete=models.SET_NULL, blank=True,null=True)
    owner = models.ForeignKey(User,verbose_name= ("Usuario"), 
                                 on_delete=models.SET_NULL, blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
