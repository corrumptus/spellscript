#imports e recursos
import glob
import os
from os import path
m_LogFileFolderPath = r'%LOCALAPPDATA%\g3\Saved\Logs'
m_FileType = '\*log'

#função que pega o log da sessão atual(proveniente do script original do mrow)
def LastestFile():
    files = glob.glob(path.expandvars(m_LogFileFolderPath) + m_FileType)
    max_file = max(files, key=os.path.getctime)
    return max_file

#carregar toda a sessão
arqpartida = open(LastestFile(), 'r', encoding = 'utf-8')
Vpartida = []
for i in arqpartida.readlines():
    if ('"DisplayName"' in i) and ('#' not in i):
        Vpartida.append(i.replace('\n', ''))
arqpartida.close()

#extrair nomes
for i in range(len(Vpartida)):
    n = Vpartida[i].find('"DisplayName"') + 15
    Vpartida[i] = Vpartida[i][n:]
    k = Vpartida[i].find('","CosmeticLoadout":')
    Vpartida[i] = Vpartida[i][:k]

#pegar os players da partida atual
arqsessao = open('Sessao.txt', 'r', encoding = 'utf-8')
Vsessao = []
for i in arqsessao:
	Vsessao.append(i.replace('\n', ''))
if Vsessao[0][19:] != LastestFile():
    arqsessao.close()
    arqsessao = open('Sessao.txt', 'w', encoding = 'utf-8')
    arqsessao.write('log de referencia: ' + LastestFile() + '\n')
    arqsessao.close()
    Vsessao = ['log de referencia: ' + LastestFile() + '\n']
Vpartida = Vpartida[len(Vsessao)-1:]

#atualiza o arquivo da sessão
arqsessao = open('Sessao.txt', 'w', encoding = 'utf-8')
for i in range(len(Vsessao)):
	arqsessao.write(Vsessao[i] + '\n')
arqsessao.write('\n'.join(Vpartida))
arqsessao.close()

#exclui nomes repetidos
listarq = []
for i in range(len(Vpartida)):
    if Vpartida[i] not in listarq:
        listarq.append(Vpartida[i])

#coloca os nomes dos players da partida no arquivo
arqpartida = open('players_atual.txt', 'w', encoding = 'utf-8')
arqpartida.write('Existem ' + str(len(listarq)) + ' players nessa partida.\n')
arqpartida.write('\n'.join(listarq))
print('Existem ' + str(len(listarq)) + ' nessa partida.')
print('\n'.join(listarq))
arqpartida.close()

#salva todas os resultados das execuções
arqsalvar = open('Salvação.txt', 'r', encoding = 'utf-8')
Vsalvar = []
for i in arqsalvar:
    Vsalvar.append(i.replace('\n',''))
arqsalvar.close()
if Vsalvar[0][19:] != LastestFile():
    arqsalvar = open('Salvação.txt', 'w', encoding = 'utf-8')
    arqsalvar.write('log de referencia: ' + LastestFile() + '\n')
else:
    arqsalvar = open('Salvação.txt', 'a', encoding = 'utf-8')
arqsalvar.write('-------------------------------------------\n')
arqsalvar.write('\n'.join(listarq)+'\n')
arqsalvar.close()