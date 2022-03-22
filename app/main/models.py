from statistics import mode
from django.db import models

from django.contrib.auth.models import AbstractUser

class BankManager(models.Manager):
    def create_bank(self, name_bank):
        book = self.create(name=name_bank, token=abs(hash(name_bank)))
        return book

class Bank(models.Model):
    name = models.CharField('Название', max_length=100)
    token = models.IntegerField('Токен', unique=True, editable=False)

    objects = BankManager()

    def __str__(self) -> str:
        return self.name

class User(AbstractUser):

    bank = models.OneToOneField(Bank, on_delete = models.CASCADE, null=True)
    
    def __str__(self):
        return self.username
