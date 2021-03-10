# Gallery
Aplicação web de uma simples galeria de imagens feita com o framework Django

# O que há no projeto
- Galeria organizada por albuns 
- Upload de imagens
- Templates responsivas feitas com Bootstrap 5
- Efeito lightbox
- Paginação

# Dependências
- python - Versão 3.5+
- Django==2.2
- django-cleanup==5.1.0
- Pillow==8.1.2
- python-decouple==3.4

# Instalação
1. Crie um ambiente virtual:
```
python3 -m venv myvenv
```
2. Ative o ambiente virtual;
3. Instale as dependências:
```
(myvenv) pip install -r requirements.txt
```
4. Em seguida você vai precisar criar um arquivo .env:
```
(myvenv) python contrib/env_gen.py
```
5. Sincronize a base de dados:
```
(myvenv) python manage.py migrate
```
6. Crie um super usuário (Administrador do sistema):
```
(myvenv) python manage.py createsuperuser
```
7. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
```
(myvenv) python manage.py runserver
```