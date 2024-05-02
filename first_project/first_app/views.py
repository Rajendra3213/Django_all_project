from django.shortcuts import render
from first_app.models import User

# Create your views here.
def index(request):
    user_list = User.objects.all()
    user_data = {'users': user_list}
    print(user_data)
    return render(request, 'first_app/index.html', context=user_data)
