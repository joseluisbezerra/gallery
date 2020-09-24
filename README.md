# Gallery
Aplicação web de uma simples galeria de imagens de campeonatos feita com o framework Django

# O que há no projeto:
- Galeria organizada por albuns 
- Upload de imagens (Óbvio rsrs)
- Templates responsivas feitas com MDBootstrap
- Efeito lightbox
- Paginação

# Dependências
- python - Versão 3.5+
- Django==2.2
- Pillow==7.2.0
- python-decouple==3.3

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