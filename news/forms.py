from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput,Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','anons','full_text','date']

        widgets={
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название'
            }),
            "anons": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class':'form-control',
                'placeholder':'Основной текст'
            
            }),
            "date": DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Дата и время публикации: ГГГГ-ММ-ДД ЧЧ:ММ:СС'
            
            }),
            
        }