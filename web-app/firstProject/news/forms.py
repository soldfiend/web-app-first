from .models import Artickle
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtickleForm(ModelForm):
    class Meta:
        model = Artickle
        fields = ['title', 'anons', 'full_text', 'data']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons статьи'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text статьи'
            })
        }
