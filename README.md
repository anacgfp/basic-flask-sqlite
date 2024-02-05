1. instala o python 3.10
2. atualiza o pip  python3 -m pip install --upgrade pip
3. instala o virtual env python3 -m pip install virtualenv
4. cria ambiente virtual python3 -m virtualenv .venv
5. se tiver no windows, vai precisar permitir rodar scripts pelo terminal pra ativar o virtual environment:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

6. ativa o venv .venv\Scripts\activate (windows)
6. se for no linux source .venv\bin\activate
7. instala as dependencias pip install -r requirements.txt
8. roda o app -> python app.py
