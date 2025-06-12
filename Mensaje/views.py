from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import Mensaje
from .forms import MensajeForm
from Cuentas.models import Usuario

class InboxView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'messages/inbox.html'
    context_object_name = 'mensajes'
    
    def get_queryset(self):
        return Mensaje.objects.filter(
            destinatario=self.request.user
        ).order_by('-fecha_envio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unread_count'] = Mensaje.objects.filter(
            destinatario=self.request.user,
            leido=False
        ).count()
        return context

class SentView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'messages/sent.html'
    context_object_name = 'mensajes'
    
    def get_queryset(self):
        return Mensaje.objects.filter(
            remitente=self.request.user
        ).order_by('-fecha_envio')

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'messages/message_detail.html'
    context_object_name = 'mensaje'
    
    def get_queryset(self):
        
        return Mensaje.objects.filter( 
            destinatario=self.request.user
        )
            
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if self.object.destinatario == request.user:
            self.object.marcar_como_leido()
        return response

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'messages/create_message.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['remitente'] = self.request.user
        
       
        if 'destinatario_id' in self.kwargs:
            kwargs['initial'] = {
                'destinatario': get_object_or_404(Usuario, pk=self.kwargs['destinatario_id'])
            }
        return kwargs
    
    def get_success_url(self):
        messages.success(
            self.request,
            _('Mensaje enviado correctamente.')
        )
        return reverse_lazy('inbox')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'destinatario_id' in self.kwargs:
            context['destinatario'] = get_object_or_404(
                Usuario, 
                pk=self.kwargs['destinatario_id']
            )
        return context

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Mensaje
    template_name = 'messages/message_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(
            self.request,
            _('Mensaje eliminado correctamente.')
        )
        return reverse_lazy('inbox')
    
    def get_queryset(self):
        
        return Mensaje.objects.filter(
            remitente=self.request.user
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_remitente'] = self.object.remitente == self.request.user
        return context