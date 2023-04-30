from django.shortcuts import render, redirect
from .forms import AtividadesModelForm
from datetime import date
from .models import AtividadesModel

def index(request):
    # Recupera o dia e mês atual
    hoje = date.today()
    dia_atual = hoje.day
    mes_atual = hoje.month

    # Busca as atividades criadas no dia e mês atual
    atividades = AtividadesModel.objects.filter(dia=dia_atual, mes=mes_atual)

    # Renderiza a página index com as atividades encontradas
    return render(request, 'index.html', {'atividades': atividades})


def cadastro(request):
    if request.method == 'POST':
        form = AtividadesModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AtividadesModelForm()
    return render(request, 'cadastro.html', {'form': form})
