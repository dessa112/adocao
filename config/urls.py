"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('adotantes/', AdotantesView.as_view(), name='adotantes'),
    path('adotados/', AdotadosView.as_view(), name='adotados'),
    path('instituicoes/', InstituicoesView.as_view(), name='instituicoes'),
    path('processos/', ProcessosView.as_view(), name='processos'),
    path('informativos/', InformativosView.as_view(), name='informativos'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... outras rotas ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from app.views import CadastroAdotadoView
from app.views import IndexView  # ou TemplateView se quiser algo simples
from app.views import AdotantesView
from app.views import AdotadosView
from app.views import InstituicoesView
from app.views import ProcessosView  # se ainda não tiver
from app.views import InformativosView  # ← importe se ainda não estiver
from app.views import CidadesView  # ← certifique-se de importar
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),  # ← ESTA LINHA É ESSENCIAL PARA O ADMIN FUNCIONAR
    path('', IndexView.as_view(), name='index'),
    path('adotantes/', AdotantesView.as_view(), name='adotantes'),
    path('adotados/', AdotadosView.as_view(), name='adotados'),
    path('adotados/cadastrar/', CadastroAdotadoView.as_view(), name='cadastro_adotado'),
    path('instituicoes/', InstituicoesView.as_view(), name='instituicoes'),
    path('processos/', ProcessosView.as_view(), name='processos'),
    path('informativos/', InformativosView.as_view(), name='informativos'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
]

from django.contrib.auth import views as auth_views

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

from django.contrib.auth import views as auth_views

urlpatterns += [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # ← adiciona o caminho usado por padrão
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]


