from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserLoginForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate


# Create your views here.

class CustomLoginView(LoginView):
    form_class = UserLoginForm

class UserCreateView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'registration/create.html'
    success_url = reverse_lazy('accounts:profile')
    def form_valid(self, form):
        print(self.request.POST['next'])
        if self.request.POST['next'] == 'back':
            return render(self.request, 'registration/create.html', {'form': form})
        elif self.request.POST['next'] == 'confirm':
            return render(self.request, 'registration/create_confirm.html', {'form': form})
        elif self.request.POST['next'] == 'regist':
            form.save()
            # 認証
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            # ログイン
            login(self.request, user)
            return super().form_valid(form)
        else:
            # 通常このルートは通らない
            return redirect(reverse_lazy('base:top'))
