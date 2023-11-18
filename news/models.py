from django.db import models

# Create your models here. 
 

class Article(models.Model):
    title=models.CharField('Name of article', max_length=50)
    anons=models.CharField('Anons', max_length=250)
    full_text=models.TextField('Acticle')
    date=models.DateTimeField('Data of published')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'