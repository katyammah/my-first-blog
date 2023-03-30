from .models import Order, Product
from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select, \
    DateInput, ClearableFileInput,  EmailField, CharField, PasswordInput
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'tel', 'email', 'question']

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


            'question': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Вопросы / пожелания'
            })
        }


class DateInput(DateInput):
    input_type = 'date'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'status', 'price', 'description', 'created_date', 'picture']

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

            'created_date': DateInput(attrs={
                'class': "form-control",
            }),

            'picture': ClearableFileInput(attrs={
                'class': "form-control",
            })
        }



User = get_user_model()


class UserCreateForm(UserCreationForm):
    email = EmailField(
        label=_("Email"),
        max_length=254,
        widget=EmailInput(attrs={'autocomplete': 'email'})
    )

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
        help_texts = {
            'password1': '',
            'password2': '',
        }
