import os
import time

def telaLimpa():
    os.system("cls")

def prosseguir():
    continuar = input("Aperte enter para utilizar o programa novamente.")
    if continuar == " ":
        telaLimpa()

print("Bem-vindo ao Zerinho ou Um. Comece a jogar para determinar o vencedor.")

nome1 = input("Escreva o seu nome, jogador 1: ")
jogada1 = int(input("Faça sua jogada: "))

nome2 = input("Escreva o seu nome, jogador 2: ")
jogada2 = int(input("Faça sua jogada: "))

nome3 = input("Escreva o seu nome, jogador 3: ")
jogada3 = int(input("Faça sua jogada: "))

def verificaJogadas():
    if jogada1 != 0 and jogada1 != 1:
        print("Jogada inválida!")
        time.sleep(0.5)
        prosseguir()
    elif jogada2 != 0 and jogada2 != 1:
        print("Jogada inválida!")
        time.sleep(0.5)
        prosseguir()
    elif jogada3 != 0 and jogada3 != 1:
        print("Jogada inválida!")
        time.sleep(0.5)
        prosseguir()

def vencedor():
    verificaJogadas()
    if jogada1 ==  jogada2 == jogada3:
        print("Empate! Ninguém venceu... Tentem novamente.")
        print("EOF")
        time.sleep(0.5)
        prosseguir()
    elif jogada1 != jogada3 and jogada1 != jogada2:
        print("O vencedor é", nome1)
        print("EOF")
        time.sleep(0.5)
        prosseguir()
    elif jogada2 != jogada3 and jogada2 != jogada1:
        print("O vencedor é", nome2)
        print("EOF")
        time.sleep(0.5)
        prosseguir()
    else:
        print("O vencedor é", nome3)
        print("EOF")
        time.sleep(0.5)
        prosseguir()

vencedor()