# Generated by Django 5.0.1 on 2024-01-07 13:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição da Doença')),
                ('cid', models.CharField(max_length=10, verbose_name='CID')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Médico')),
            ],
        ),
        migrations.CreateModel(
            name='TipoAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Tipo de Atendimento')),
            ],
        ),
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_atendimento', models.DateField(default=django.utils.timezone.now, verbose_name='Data do Atendimento')),
                ('id_boletim', models.CharField(max_length=20, verbose_name='ID do Boletim')),
                ('periodo', models.CharField(choices=[('diurno', 'Diurno'), ('noturno', 'Noturno')], max_length=10, verbose_name='Período')),
                ('revisao', models.BooleanField(verbose_name='Revisão')),
                ('exame_imagem', models.BooleanField(verbose_name='Exame de Imagem')),
                ('exame_laboratorio', models.BooleanField(verbose_name='Exame de Laboratório')),
                ('dor_toracica', models.BooleanField(verbose_name='Dor Torácica')),
                ('sepse', models.BooleanField(verbose_name='Sepse')),
                ('sincope', models.BooleanField(verbose_name='Síncope')),
                ('prescricao', models.BooleanField(verbose_name='Prescrição')),
                ('doenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimentos.doenca', verbose_name='Doença')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimentos.medico', verbose_name='Médico que Realizou')),
                ('tipo_atendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atendimentos.tipoatendimento', verbose_name='Tipo de Atendimento')),
            ],
        ),
    ]
