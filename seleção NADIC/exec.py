from time import sleep
from classes import*
import pygame
import os

opcao = 's'
cpf_dados = []
Fulano = 0
Ciclano = 0
Beltrano = 0

lista_candidatos = f'''
{c1}\n
{c2}\n 
{c3}
'''
    
while opcao == 's':
      
    os.system('cls')
    print('--------------')
    print('ELEIÇÕES NADIC\n')
    print('MENU: \nCANDIDATOS = 1\nVOTAR = 2\nRESULTADO = 3')
    print('--------------\n')
    
    exec = input('Selecione a ação: ')
    os.system('cls')
    if exec == '1':
        print('----------')
        print('CANDIDATOS:\n')
        print(lista_candidatos)
        print('----------\n')
        
        input('PRESSIONE ENTER PARA SAIR')
        os.system('cls')
    elif exec == '2':
        cpf = input('Informe seu CPF: ')
        if cpf not in cpf_dados:
            cpf_dados.append(cpf)
            candidato = input('Insira o número do candidato: ')
            if candidato == '1':
                Fulano+=1
            elif candidato == '2':
                Ciclano+=1
            elif candidato == '3':
                Beltrano+=1
            os.system('cls')
            print('VOTO COMPUTADO COM SUCESSO')
            pygame.init()
            pygame.mixer.music.set_volume(0.50)
            pygame.mixer.music.load('song/urna.mp3')
            pygame.mixer.music.play()
            sleep(1)
        else:
            print('\nCPF com voto ja computado!!!\n')
            input('PRESSIONE ENTER PARA SAIR')
            os.system('cls')   
    elif exec == '3':
        key = input('Digite a senha: ')
        os.system('cls')
        
        if key == '123456789':
            print('RESULTADO DA ELEIÇÃO\n')
            print('FULANO: ' + str(Fulano)) 
            print('CICLANO: ' + str(Ciclano)) 
            print('BELTRANO: ' + str(Beltrano))
            arquivo = open('resultado/RESULTADO DA ELEIÇÃO.txt','w')
            arquivo.write('RESULTADO DA ELEIÇÃO\n\n')
            arquivo.write('FULANO: ' + str(Fulano) + '\n')
            arquivo.write('CICLANO: ' + str(Ciclano) + '\n')
            arquivo.write('BELTRANO: ' + str(Beltrano) + '\n')
            arquivo.close()
            input('\nAPERTE ENTER PARA SAIR')
        else:
            print('Senha incorreta\n')
            input('PRESSIONE ENTER PARA SAIR')            
        os.system('cls')
    opcao = 's'