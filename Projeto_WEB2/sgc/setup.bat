@echo off
echo ========================================
echo  TechFix SGC - Configuracao Inicial
echo ========================================
echo.

echo Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERRO ao instalar dependencias.
    pause
    exit /b 1
)

echo.
echo Criando banco de dados...
python manage.py makemigrations clientes produtos vendas
python manage.py migrate

echo.
echo Criando usuario admin...
echo from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@techfix.com', 'admin123') | python manage.py shell

echo.
echo Pronto!
echo.
echo ========================================
echo  Para iniciar o sistema:
echo    python manage.py runserver
echo.
echo  Acesse: http://localhost:8000/login/
echo  Usuario: admin
echo  Senha:   admin123
echo ========================================
pause
