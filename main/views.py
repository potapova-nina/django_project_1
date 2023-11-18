from django.shortcuts import render

# Create your views here.
# in templates

def index(request):
    data={
        'title': 'Главная страница',
        'values':['Some','hello','123'],
        'obj':{
            'car':'BMW',
            'age':18,
            'hobby':'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

