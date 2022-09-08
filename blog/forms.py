from .models import Order
from django.forms import ModelForm, TextInput, EmailInput, Textarea



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
