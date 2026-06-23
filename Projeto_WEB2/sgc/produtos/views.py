from django.shortcuts import render

def lista(request):
    return render(request, 'produtos/lista.html')

def form(request, pk=None):
    return render(request, 'produtos/form.html', {'produto_id': pk})
