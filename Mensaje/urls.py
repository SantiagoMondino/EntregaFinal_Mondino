from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (
    InboxView,
    SentView,
    MessageDetailView,
    MessageCreateView,
    MessageDeleteView
)

urlpatterns = [
    path('', InboxView.as_view(), name='inbox'),
    path(_('sent/'), SentView.as_view(), name='sent'),
    path(_('new/'), MessageCreateView.as_view(), name='create_message'),
    path(_('new/<int:destinatario_id>/'), MessageCreateView.as_view(), name='create_message_to'),
    path(_('<int:pk>/'), MessageDetailView.as_view(), name='message_detail'),
    path(_('<int:pk>/delete/'), MessageDeleteView.as_view(), name='delete_message'),
]