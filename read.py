#Método open -> Abre um arquivo txt
arquivo = open('Alunos.txt', 'r')
"""Usamos 'r' para abrir o arquivo para ler (read), 'w' quando estamos abrindo o 
arquivo para escrever (write) ou 'a' se formos adicionar (append) uma informação
no arquivo."""

#Com o arquivo aberto (open), agora efetivamente podemos ler o arquivo (read)!

#Método read()
#print(arquivo.read()) ou
#Método readlines()
print(arquivo.readlines()) #formato de lista - cada item da lista é uma linha.

