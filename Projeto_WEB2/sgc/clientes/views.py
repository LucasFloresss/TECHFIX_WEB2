from django.shortcuts import render

def lista(request):
    return render(request, 'clientes/lista.html')

def form(request, pk=None):
    return render(request, 'clientes/form.html', {'cliente_id': pk})
