from django.urls import path
from . import views  # Importando as views da aplicação core

urlpatterns = [
    path('', views.index, name='index'),  # Rota principal
    path('comment/', views.comment_view, name='comment'),  # Rota para o formulário de comentários
]

