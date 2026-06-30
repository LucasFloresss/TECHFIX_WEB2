from django.shortcuts import render

def index(request):
    return render(request, 'relatorios/index.html') #carrega o template relatorios/index.html quando o usuário acessa a página de relatórios.
