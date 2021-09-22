from .models import Partnumbers, MassPartnumbers
from django.forms import ModelForm, TextInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Partnumbers
        fields = ['partnumber']

        widgets = {
            'partnumber': TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Введите значение'})
        }

class NumbersForm (ModelForm):
    class Meta:
        model = MassPartnumbers
        fields = ['value_a', 'value_b']

        widgets = {
            'value_a': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'placeholder': 'Начальная позиция',
                'value': '',
            }),
            'value_b': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'placeholder': 'Конечная позиция',
                'value': '',
            }),
        }