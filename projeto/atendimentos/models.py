# models.py

from django.utils import timezone
from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Médico')

    def __str__(self):
        return self.nome

class Doenca(models.Model):
    descricao = models.CharField(max_length=255, verbose_name='Descrição da Doença')
    cid = models.CharField(max_length=10, verbose_name='CID')

    def __str__(self):
        return f"{self.cid} - {self.descricao}"

class TipoAtendimento(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Tipo de Atendimento')

    def __str__(self):
        return self.nome

class Boletim(models.Model):
    data_atendimento = models.DateField(verbose_name='Data do Atendimento', default=timezone.now)
    id_boletim = models.CharField(max_length=20, verbose_name='ID do Boletim')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico que Realizou')
    periodo = models.CharField(max_length=10, choices=[('diurno', 'Diurno'), ('noturno', 'Noturno')], verbose_name='Período')
    tipo_atendimento = models.ForeignKey(TipoAtendimento, on_delete=models.CASCADE, verbose_name='Tipo de Atendimento')
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE, verbose_name='Doença')
    revisao = models.BooleanField(verbose_name='Revisão')
    exame_imagem = models.BooleanField(verbose_name='Exame de Imagem')
    exame_laboratorio = models.BooleanField(verbose_name='Exame de Laboratório')
    dor_toracica = models.BooleanField(verbose_name='Dor Torácica')
    sepse = models.BooleanField(verbose_name='Sepse')
    sincope = models.BooleanField(verbose_name='Síncope')
    prescricao = models.BooleanField(verbose_name='Prescrição')

    def __str__(self):
        return f"Boletim {self.id_boletim} - {self.medico} - {self.data_atendimento}"
