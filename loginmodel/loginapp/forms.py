from django import  forms
from loginapp.models import User

class NewUserform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
