import csv
import logging
import io
from django.shortcuts import render, get_object_or_404, redirect
from .models import Medico, Doenca, TipoAtendimento, Boletim
from .forms import MedicoForm, BoletimForm, AdicionarMedicosCSVForm

# Create your views here.

# Geral
def pagina_inicial(request):
    total_medicos = Medico.objects.count()
    total_boletins = Boletim.objects.count()
    return render(request, 'pagina_inicial.html',{
        'total_medicos': total_medicos,
        'total_boletins': total_boletins
    })

# CRUD de médicos
def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'lista_medicos.html', {'medicos': medicos})

def detalhes_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    return render(request, 'detalhes_medico.html', {'medico': medico})

def adicionar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicos')
    else:
        form = MedicoForm()
    return render(request, 'adicionar_medico.html', {'form': form})

def editar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect(lista_medicos)
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'editar_medico.html', {'form': form, 'medico': medico})

def excluir_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect(lista_medicos)
    return render(request, 'excluir_medico.html', {'medico': medico})

def adicionar_medicos_csv(request):
    if request.method == 'POST':
        form = AdicionarMedicosCSVForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo_csv = request.FILES.get('arquivo_csv')
            if arquivo_csv:
                # Processar o arquivo CSV e adicionar médicos
                try:
                    # Utilize a biblioteca chardet para detectar automaticamente a codificação
                    import chardet
                    rawdata = arquivo_csv.read()
                    resultado = chardet.detect(rawdata)
                    codificacao = resultado['encoding']

                    # Volte ao início do arquivo antes de ler com a codificação detectada
                    arquivo_csv.seek(0)
                    
                    dados_csv = csv.DictReader(io.TextIOWrapper(arquivo_csv, encoding=codificacao))
                    if 'nome' in dados_csv.fieldnames:
                        for linha in dados_csv:
                            if 'nome' in linha:
                                logging.info(f'Processando linha: {linha}')  # Adicione um log
                                Medico.objects.create(nome=linha['nome'])  # Ajuste conforme seus campos
                        return redirect('lista_medicos')
                    else:
                        raise ValueError("O cabeçalho do arquivo não contém a coluna 'nome'")
                except (csv.Error, ValueError) as e:
                    logging.error(f'Erro durante o processamento do CSV: {e}')  # Adicione um log
                    pass
    else:
        form = AdicionarMedicosCSVForm()

    return render(request, 'adicionar_medicos_csv.html', {'form': form})

# CRUD de Boletins

def lista_boletins(request):
    boletins = Boletim.objects.all()
    return render(request, 'lista_boletins.html', {'boletins': boletins})

def detalhes_boletim(request, pk):
    boletim = get_object_or_404(Boletim, pk=pk)
    return render(request, 'detalhes_boletim.html', {'boletim': boletim})

def adicionar_boletim(request):
    if request.method == 'POST':
        form = BoletimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_boletins')
    else:
        form = BoletimForm()
    return render(request, 'adicionar_boletim.html', {'form': form})

def editar_boletim(request, pk):
    boletim = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = BoletimForm(request.POST, instance=boletim)
        if form.is_valid():
            form.save()
            return redirect(lista_boletins)
    else:
        form = BoletimForm(instance=boletim)
    return render(request, 'editar_boletim.html', {'form': form, 'boletim': boletim})

def excluir_boletim(request, pk):
    boletim = get_object_or_404(Boletim, pk=pk)
    if request.method == 'POST':
        boletim.delete()
        return redirect(lista_boletins)
    return render(request, 'excluir_boletim.html', {'boletim': boletim})