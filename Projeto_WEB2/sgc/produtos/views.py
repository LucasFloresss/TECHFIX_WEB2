from django.shortcuts import render

def lista(request):
    return render(request, 'produtos/lista.html') #Renderiza o template produtos/lista.html

def form(request, pk=None): #Exibe formulário para criar/editar um produto, sem pk
    return render(request, 'produtos/form.html', {'produto_id': pk}) # saber se é criação ou edição
