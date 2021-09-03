
from django.contrib.auth        import get_user_model
from django                     import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, label='Usuario:',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, label='Contraseña:',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=30, required=True, label='Repita contraseña:',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=50, required=False, label='Email:',widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, label='Nombre:',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, label= 'Apellido:',widget=forms.TextInput(attrs={'class':'form-control'}))
    comparte = forms.BooleanField(required=False, label='Compartir mis resultados:',widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            

    class Meta:
        User = get_user_model()
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
