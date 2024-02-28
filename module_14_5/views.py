from django.shortcuts import render
from .forms import DemoForm

def home(request):
    form = DemoForm()
    if request.method == 'POST':
        form = DemoForm(request.POST)
    
    return render(request, "index.html", {'form': form})