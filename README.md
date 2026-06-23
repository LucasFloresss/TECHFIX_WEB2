TechFix SGC — Sistema de Gestão Comercial

Alunos:
Lucas Gomes
Mariana Borel
Susana Borges
Gabriel Guedes
Marcos Vinicius

Tecnologias Utilizadas

* Python
* Django 4.2
* Django REST Framework
* JWT para autenticação
* SQLite
* HTML, CSS e JavaScript

Estrutura do Projeto

* core → Configurações principais
* clientes → Cadastro de clientes
* produtos → Cadastro de produtos
* vendas → Controle de vendas
* relatorios → Relatórios do sistema
* templates → Páginas HTML
* static → Arquivos CSS e JavaScript
* manage.py
* requirements.txt
* setup.bat
* criar_usuarios.py

Como Executar

1. Instale as dependências:

pip install -r requirements.txt

2. Crie o banco de dados:

python manage.py makemigrations clientes produtos vendas

python manage.py migrate

3. Crie os usuários:

python criar_usuarios.py

4. Inicie o servidor:

python manage.py runserver

5. Acesse no navegador:

http://localhost:8000/login/

Usuários Padrão

| Usuário     | Senha    | Perfil        |
| ----------- | -------- | ------------- |
| admin       | admin123 | Administrador |
| funcionario | func123  | Funcionário   |

API REST

Autenticação

* POST /auth/login → Gerar token JWT

Clientes

* GET /api/clientes/ → Listar clientes
* POST /api/clientes/ → Cadastrar cliente
* GET /api/clientes/{id}/ → Buscar cliente
* PUT /api/clientes/{id}/ → Atualizar cliente
* DELETE /api/clientes/{id}/ → Excluir cliente

Produtos

* GET /api/produtos/ → Listar produtos
* POST /api/produtos/ → Cadastrar produto
* GET /api/produtos/{id}/ → Buscar produto
* PUT /api/produtos/{id}/ → Atualizar produto
* DELETE /api/produtos/{id}/ → Excluir produto

Vendas

* GET /api/vendas/ → Listar vendas
* POST /api/vendas/ → Registrar venda
* GET /api/vendas/{id}/ → Consultar venda

Relatórios

* GET /api/relatorios/periodo/ → Vendas por período
* GET /api/relatorios/cliente/ → Vendas por cliente
* GET /api/relatorios/anual/ → Faturamento anual

Regras de Negócio

* CPF não pode ser repetido
* Clientes com vendas não podem ser excluídos
* Produtos não podem ter preço negativo
* Toda venda deve possuir itens
* Estoque é atualizado automaticamente
* Não é permitido vender sem estoque suficiente
* O valor total da venda é calculado automaticamente

Obs: Feito no sqlite pois o XAMPP sempre dá problema na faculdade kkkkkkk
