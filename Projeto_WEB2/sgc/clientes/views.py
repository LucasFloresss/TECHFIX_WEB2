from django.shortcuts import render

def lista(request):
    return render(request, 'clientes/lista.html') #  lista todos os clientes

def form(request, pk=None):
    return render(request, 'clientes/form.html', {'cliente_id': pk}) # exibe formulário para criar/editar um cliente

 # Controla a lógica de negócio e o fluxo HTTP. Cada função recebe uma requisição e retorna uma resposta.
