from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Enter valid Email',
    )

    class Meta:
        model = User
        fields = ('username','email','password1','password2',)
        # __all__ = forms.TextInput(widget=forms.TextInput(attrs={'class': 'form-control'})
            
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    