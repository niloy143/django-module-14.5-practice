from django.shortcuts import render
from .forms import DemoModelForm

def model_form(request):
    form = DemoModelForm()
    if request.method == 'POST':
        form = DemoModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    
    return render(request, "model_form.html", {'form': form})