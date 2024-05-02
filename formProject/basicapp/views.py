from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    print("view function called")
    form = forms.FormName()
    if request.method == 'POST':
        print("valid")
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Form validation successful")
            print("Name: " + form .cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
        else:
            print("error")

    return render(request, 'basicapp/form_page.html', {'form': form})


# Create your views here.
