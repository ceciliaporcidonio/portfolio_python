from django.contrib import admin
from django.urls import path, include  # Inclua o include para importar URLs de outras aplicações

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o admin
    path('', include('core.urls')),  # Importa as rotas da aplicação 'core'
]

