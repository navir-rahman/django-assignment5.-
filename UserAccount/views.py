from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from . forms import UserRegistration, UserUpdateForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import login, logout
from django.views import View


class SignUp(FormView):
    template_name= 'signup.html'
    form_class = UserRegistration
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserUpdateView(View):
    template_name = 'signup.html'
    
    def get(self, request):
        form =UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            reverse_lazy('profile') 

        return render(request, self.template_name, {'form': form})


class ChangePasswordForm(PasswordChangeView):
    template_name = "passwordreset.html"
    success_url = reverse_lazy('profile')
    