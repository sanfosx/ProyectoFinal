
from django.contrib.auth        import get_user_model
from django                     import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Su Nombre')
    last_name = forms.CharField(max_length=30, required=False, label= 'Su Apellido')
    comparte = forms.BooleanField(required= False, label='Deseo compartir mis resultados')
    



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            

    class Meta:
        User = get_user_model()
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
