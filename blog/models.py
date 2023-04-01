from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Order(models.Model):
    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'

    name = models.CharField('Имя и фамилия', max_length=50)
    tel = models.CharField('Телефон', max_length=20)
    email = models.CharField('Email', max_length=20)
    question = models.TextField('Вопросы')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    class StatusOfProduct(models.TextChoices):
        ready = '(готовый товар)', ('готовый товар')
        to_order = '(на заказ)', ('на заказ')

    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=200)
    status = models.CharField("Статус товара", max_length=20, choices=StatusOfProduct.choices)
    price = models.IntegerField("Цена")
    picture = models.ImageField("Изображение", null=True, upload_to='images/')
    description = models.TextField("Описание товара")
    created_date = models.DateTimeField('Дата занесения товара в каталог', default=timezone.now)

    def __str__(self):
        return self.title


class User(AbstractUser):
    bio = models.TextField('Описание пользователя', max_length=500, null=True)


class Basket(models.Model):
    class Meta:
        verbose_name = u'Корзина'
        verbose_name_plural = u'Корзины'

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя {self.user} - Товар {self.product}'
