from time import sleep
from classes import*
import pygame
import os

opcao = 's'
cpf_dados = []
votos = {}

candidatos = {
    '1': 'Fulano',
    '2': 'Ciclano',
    '3': 'Beltrano'
}

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
            voto = input('Digite o número do candidato: ')
            if voto in candidatos: # se é um dos números de candidato válido
                votos[voto] = votos.get(voto, 0) + 1
                
                os.system('cls')
                print('VOTO COMPUTADO COM SUCESSO')
                pygame.init()
                pygame.mixer.music.set_volume(0.50)
                pygame.mixer.music.load('song/urna.mp3')
                pygame.mixer.music.play()
                sleep(1)
            else:
                print(f'Número inválido: {voto}')
                input('PRESSIONE ENTER PARA SAIR')
        else:
            print('\nCPF com voto ja computado!!!\n')
            input('PRESSIONE ENTER PARA SAIR')
            os.system('cls')   
    elif exec == '3':
        key = input('Digite a senha: ')
        os.system('cls')
        
        if key == '123456789':
            
            print('RESULTADO\n')
            for numero, qtd_votos in votos.items():
                print(f'{candidatos[numero]}: {qtd_votos}')
            input('\nAPERTE ENTER PARA SAIR')
        else:
            print('Senha incorreta\n')
            input('PRESSIONE ENTER PARA SAIR')            
        os.system('cls')
    opcao = 's'