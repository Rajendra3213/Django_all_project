from django.shortcuts import render
from loginapp.forms import NewUserform

# Create your views here.
def index(request):
    return render(request, 'loginapp/index.html')

def users(request):
    form = NewUserform()
    if request.method == 'POST':
        form = NewUserform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error from invalid")

    return render(request, 'loginapp/login.html', {'form': form})



