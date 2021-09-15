from .models import Partnumbers
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
