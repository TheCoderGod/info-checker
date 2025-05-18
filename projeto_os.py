import os
import platform
from datetime import datetime

usuario = os.environ.get('USERNAME') or os.environ.get('USER')
pasta_home = os.path.expanduser('~')
sistema = platform.system()
arquivos = []
pastas = []

print('---------------------------------')
print(f'Olá, {usuario} - Sistema: {sistema}')
print('Data de execução:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('---------------------------------\n')

print(f'📁 Pasta atual do script: {os.path.abspath(__file__)}')
print(f'📁 Diretório onde estou sendo executado: {os.getcwd()}\n')

os.chdir(pasta_home)

print(f'🔁 Mudando para a pasta home: {pasta_home}... OK!\n')
print('📋 Listando arquivos e pastas...\n')

for objeto in os.listdir():
    caminho = os.path.join(pasta_home, objeto)
    if os.path.isfile(caminho):
        arquivos.append(objeto)
    else:
        pastas.append(objeto)

print('📄 Arquivos encontrados:')
for arq in arquivos:
    print(f'  - {arq}')

print('\n📁 Pastas encontradas:')
for pst in pastas:
    print(f'  - {pst}')
