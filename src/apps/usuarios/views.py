from django.contrib.auth                import login, authenticate
from django.shortcuts                   import render, redirect
from django.urls                        import reverse_lazy
from .forms                             import SignUpForm
from django.contrib.auth.mixins         import LoginRequiredMixin
from django.views.generic               import ListView
from .models                            import Usuario

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            """username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)"""
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'usuarios/signup.html', {'form': form})

def login(request):

	return render(request, 'ususarios/login.html')

class ListarUsuarios(LoginRequiredMixin, ListView):

    template_name = "usuarios/listar.html"
    model = Usuario
    context_object_name = 'usuarios'

    def get_queryset(self):
        if self.request.user.is_staff:
            print("A VER QUE GUARDA",Usuario.objects.all())
            return Usuario.objects.all()