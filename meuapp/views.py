from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timezone
import zoneinfo

def home(request):
    local_timezone = zoneinfo.ZoneInfo("Brazil/East")
    hora_atual = datetime.now(local_timezone).hour

    # print(zoneinfo.available_timezones())

    if(5<=hora_atual < 12):
        mensagem = "Bom dia"
    elif(12<=hora_atual<18):
        mensagem = "Boa tarde"
    else:
        mensagem = "Boa noite"
    return HttpResponse(f"Olá Mundjo! Hora atual: {str(hora_atual)}horas -> {mensagem}!")

def saudacao(request, nome):
    mensagem = f'Olá, bem vindo {nome}!'
    return HttpResponse(mensagem)

def produtos(request, id_produto):
    produtos = {
        1: 'Notebook',
        2: 'Teclado',
        3: 'Mouse'
    }

    produto = produtos.get(id_produto, "Produto não encontrado")

    return HttpResponse(f"Detalhes do produto: {produto}")


