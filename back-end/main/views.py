from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import YourModelForm
from django.contrib import messages
from .models import YourModel
# Create your views here.

def signin(request):
    return render(request, 'main/signin.html')
def index(request):
    your_model_data = YourModel.objects.all()  # Получаем данные из модели, если они доступны
    context = {
        'your_model_data': your_model_data,
    }
    return render(request, 'main/index.html', context)
def about(request):
    return render(request, 'main/creators.html')
def addyourtip(request):
    return render(request, 'main/form.html')
def java(request):
    return render(request, 'main/java.html')
def python(request):
    return render(request, 'main/python.html')
def form_view(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
    else:
        form = YourModelForm()
    return render(request, 'main/your_template.html', {'form': form})
