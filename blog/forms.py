from .models import Order, Product
from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select, DateInput, ClearableFileInput
from PIL import Image

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'tel', 'email', 'adress', 'question']

        widgets = {


            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Имя и Фамилия'
            }),

            'tel': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Телефон'
            }),

            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
            }),

            'adress': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Ваш адрес'
            }),

            'question': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Вопросы / пожелания'
            })
        }


class DateInput (DateInput):
    input_type = 'date'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'status', 'price',  'description', 'created_date', 'picture']

        widgets = {


            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название'
            }),

            'status': Select(attrs={
                'class': "form-control",
            }),

            'price': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Цена'
            }),

            'description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Описание товара'
            }),

            'created_date': DateInput (attrs={
                'class': "form-control",
            }),

            'picture': ClearableFileInput(attrs={
                'class': "form-control",

            })
        }

