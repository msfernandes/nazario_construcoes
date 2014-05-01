
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.db.models import Sum

from django.contrib.auth.decorators import login_required

from relatorios import TotalCategoria, TotalEtapa, Clientes

from gerenciador_contatos.models import *
from gerenciador_despesas.models import *

from outros.models import Mes
# Create your views here.


def home(request):
    if not request.user.is_authenticated():
        return redirect('/admin/')
    else:
        lista_obras = Obra.objects.all().order_by(
            'cliente__nome'
        )

        meses = Mes.objects.all()

        return render_to_response('home.html', {
            'lista_obras': lista_obras,
            'meses': meses,
        }, context_instance=RequestContext(request))


def contatos(request):
    clientes = Cliente.objects.all()

    lista_telefones = []
    lista_clientes = []
    lista_fornecedores = []

    for cliente in clientes:
        dados_cliente = Clientes()

        dados_cliente.cliente = cliente

        dados_cliente.telefones = TelefoneCliente.objects.filter(
            cliente=cliente.id
        ).order_by('cliente')

        dados_cliente.obras = Obra.objects.filter(
            cliente=cliente.id
        ).order_by('cliente')

        lista_clientes.append(dados_cliente)

    lista_fornecedores = TelefoneFornecedor.objects.all().order_by(
        'fornecedor__nome'
    )

    lista_contas = Conta.objects.all().order_by(
        'titular'
    )

    return render_to_response('contatos.html', {
        'lista_telefones': lista_telefones,
        'lista_clientes': lista_clientes,
        'lista_fornecedores': lista_fornecedores,
        'lista_contas': lista_contas
    }, context_instance=RequestContext(request))


def obras(request):
    obra = request.POST["obra"]
    mes = request.POST['mes']
    ano = request.POST['ano']

    obra = Obra.objects.filter(id=obra)
    obra = obra[0]

    boletos = Boleto.objects.filter(
        despesa__obra=obra,
        vencimento__month=mes,
        vencimento__year=ano
    ).order_by('pago', 'vencimento')

    boletos_categoria = Boleto.objects.values(
        'despesa__categoria__descricao'
    ).filter(
        despesa__obra=obra,
        vencimento__month=mes,
        vencimento__year=ano
    ).annotate(valor_categoria=Sum('valor'))

    total_categoria = []

    for boleto in boletos_categoria:
        valor_categoria = []

        valor_categoria = TotalCategoria(
            boleto['despesa__categoria__descricao'],
            boleto['valor_categoria']
        )

        total_categoria.append(valor_categoria)

    boletos_etapa = Boleto.objects.values(
        'despesa__etapa__descricao'
    ).filter(
        despesa__obra=obra,
        vencimento__month=mes,
        vencimento__year=ano
    ).annotate(valor_etapa=Sum('valor'))

    total_etapa = []

    for boleto in boletos_etapa:
        valor_etapa = []

        valor_etapa = TotalEtapa(
            boleto['despesa__etapa__descricao'],
            boleto['valor_etapa']
        )

        total_etapa.append(valor_etapa)

    return render_to_response('obras.html', {
        'obra': obra,
        'boletos': boletos,
        'total_categoria': total_categoria,
        'total_etapa': total_etapa,
    }, context_instance=RequestContext(request))


def resumo_obra(request):
    return render_to_response(
        'resumo.html',
        context_instance=RequestContext(request)
    )
