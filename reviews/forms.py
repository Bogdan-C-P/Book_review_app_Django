from django.forms import ModelForm
from reviews.models import Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields =  ['rating', 'comment']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        