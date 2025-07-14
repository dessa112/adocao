from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Cidade, Adotante, Adotado, Instituicao, ProcessoAdocao, Informativo

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AdotantesView(View):
    def get(self, request, *args, **kwargs):
        adotantes = Adotante.objects.all()
        return render(request, 'adotantes.html', {'adotantes': adotantes})


class AdotadosView(View):
    def get(self, request, *args, **kwargs):
        adotados = Adotado.objects.all()
        return render(request, 'adotados.html', {'adotados': adotados})


class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})


class ProcessosView(View):
    def get(self, request, *args, **kwargs):
        processos = ProcessoAdocao.objects.all()
        return render(request, 'processos.html', {'processos': processos})


class InformativosView(View):
    def get(self, request, *args, **kwargs):
        informativos = Informativo.objects.all()
        return render(request, 'informativos.html', {'informativos': informativos})


class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})
    
from django.views import View
from django.shortcuts import render, redirect
from .forms import AdotadoForm
from .models import Adotado

class CadastroAdotadoView(View):
    def get(self, request, *args, **kwargs):
        form = AdotadoForm()
        return render(request, 'cadastro_adotado.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AdotadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/adotados/')
        return render(request, 'cadastro_adotado.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Adotado, Adotante

@method_decorator(login_required, name='dispatch')
class AdotadosView(View):
    def get(self, request, *args, **kwargs):
        # Verifica se o usuário está vinculado a um adotante autorizado
        try:
            adotante = Adotante.objects.get(email=request.user.email)
            if not adotante.autorizado:
                return render(request, 'nao_autorizado.html')
        except Adotante.DoesNotExist:
            return render(request, 'nao_autorizado.html')

        adotados = Adotado.objects.all()
        return render(request, 'adotados.html', {'adotados': adotados})
