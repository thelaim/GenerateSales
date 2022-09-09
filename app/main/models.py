
from django.db import models

from django.contrib.auth.models import AbstractUser

#----------MANAGER---------------

class ProductManager(models.Manager):

    def find_product(self, name_bank):
        return super().get_queryset().filter(bank__name=name_bank)



#--------------MODELS-------------


class Bank(models.Model):
    name = models.CharField('Название', max_length=100)
    token = models.IntegerField('Токен', unique=True, editable=False)

    def __str__(self) -> str:
        return self.name

class User(AbstractUser):

    bank = models.OneToOneField(Bank, on_delete = models.CASCADE, null=True)
    
    def __str__(self):
        return self.username

class CategoryProduct(models.Model):
    name = models.CharField('Категория продукта', max_length=30)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField('Название продукта', max_length=100)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Категория продукта', null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name='Банк', null=True)
    percent_user = models.IntegerField('Процент партнеру банка', default=1)
    percent_bank = models.IntegerField('Процент по продукту для банка', default=5)

    objects = models.Manager()
    product_objects = ProductManager()

    class Meta:
        default_manager_name = 'product_objects'

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    income = models.DecimalField(decimal_places=2, max_digits=10, default=13000)
    email_client = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=11) #дописать валидаторы
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    token_bank = models.IntegerField(blank=True, null=True)
    view = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email_client
    
