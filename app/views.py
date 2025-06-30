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
