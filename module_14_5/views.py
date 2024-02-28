from django.shortcuts import render
from .forms import DemoForm

def home(request):
    form = DemoForm()
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    
    return render(request, "index.html", {'form': form})