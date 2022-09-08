from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
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
    name = models.CharField('Имя и фамилия', max_length=50)
    tel = models.CharField('Телефон', max_length=20)
    email = models.CharField('Email', max_length=20)
    adress = models.TextField('Адрес')
    question= models.TextField('Вопросы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'