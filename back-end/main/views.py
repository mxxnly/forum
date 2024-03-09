from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import YourModelForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'main/index.html')
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
            return redirect('index')  # Замените 'success_url' на URL, куда вы хотите перенаправить после успешной отправки формы
    else:
        form = YourModelForm()
    return render(request, 'main/your_template.html', {'form': form})
