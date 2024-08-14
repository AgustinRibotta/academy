from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.shortcuts import redirect
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        Student.objects.create(
            user=user,
            fname=user.username,
            lname='',
            email=user.email,
            date_of_birth='2000-01-01'  # Valor por defecto
        )
        auth_login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            auth_login(self.request, user)
            return redirect(self.get_success_url())
        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')

class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('login')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['fname', 'lname', 'email', 'date_of_birth']
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return Student.objects.get(user=self.request.user)
    
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'student/confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        Student.objects.filter(user=user).delete()  # Eliminar el perfil del estudiante
        response = super().delete(request, *args, **kwargs)
        return response
