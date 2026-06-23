from django.shortcuts import render

def lista(request):
    return render(request, 'vendas/lista.html')

def nova(request):
    return render(request, 'vendas/form.html')

def detalhe(request, pk):
    return render(request, 'vendas/detalhe.html', {'venda_id': pk})
