"""
'w' -> serve para escrever no arquivo mas se o arquivo já existia, ele irá substituir o arquivo.
'a' -> serve para escrever no arquivo mas apenas irá adicionar novas informações e não irá substituir.
"""
novo_arquivo = open('Resumo.txt', 'w')
novo_arquivo.write('Olá, meu nome é Larissa!\nPrazer.\n') #\n dá enter e escreve em outra linha
novo_arquivo.write('Terceira linha...')
novo_arquivo.close() #para fechar e salvar o arquivo

"""
Estrutura 'with'

with open('NomeArquivo.txt', 'w') as arquivo:
    arquivo.write()
    ...
    
Usando a estrutura with: ao final do with, a própria estrutura with fecha
automaticamente o arquivo. Então não precisa executar o .close().
"""