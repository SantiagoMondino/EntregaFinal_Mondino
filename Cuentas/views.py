from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView
)
from django.views.generic import (
    CreateView, 
    UpdateView, 
    DetailView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from .forms import (
    SignUpForm, 
    ProfileUpdateForm, 
    CustomPasswordChangeForm
)
from .models import Usuario
from Escuela.models import Post

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Iniciar Sesión')
        return context

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Has cerrado sesión correctamente.'))
        return super().dispatch(request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Registro de Usuario')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            _('¡Registro exitoso! Por favor inicia sesión con tus credenciales.')
        )
        return response

class ProfileView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_user'
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        
        context['title'] = _('Mi Perfil')
        context['posts_count'] = Post.objects.filter(autor=user).count()
        context['comments_count'] = user.comentario_set.count()
        context['user_posts'] = Post.objects.filter(autor=user).order_by('-fecha_publicacion')[:5]
        
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Editar Perfil')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _('Perfil actualizado correctamente.'))
        return super().form_valid(form)

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Cambiar Contraseña')
        return context
    
    def form_valid(self, form):
        messages.success(self.request, _('Contraseña cambiada correctamente.'))
        return super().form_valid(form)