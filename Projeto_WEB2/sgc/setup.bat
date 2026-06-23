@echo off
echo ========================================
echo  TechFix SGC - Configuracao Inicial
echo ========================================
echo.

echo [1/4] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERRO ao instalar dependencias. Verifique seu Python/pip.
    pause
    exit /b 1
)

echo.
echo [2/4] Criando banco de dados...
python manage.py makemigrations clientes produtos vendas
python manage.py migrate

echo.
echo [3/4] Criando usuario admin...
echo from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@techfix.com', 'admin123') | python manage.py shell

echo.
echo [4/4] Pronto!
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
