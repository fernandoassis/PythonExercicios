#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3:
# Será tocada a música: The Imperial March (Darth Vader's Theme)
#Importa as bibliotecas pygame e time. Pode ser que precise instalar a biblioteca pygame
import pygame
import time
#Inicia a biblioteca pygame
pygame.init()
#Dá o comando de ler o arquivo de música
pygame.mixer.music.load('021.mp3')
#Dá o play na música
pygame.mixer.music.play()
# Aguarde a duração da música antes de encerrar o programa
while pygame.mixer.music.get_busy():
    time.sleep(1)
#Neste código, adicionamos um loop while que aguarda até que a música tenha terminado de tocar antes de encerrar o programa. 
#O time.sleep(1) faz com que o programa aguarde 1 segundo antes de verificar se a música ainda está tocando. 
#Isso garante que o programa aguarde a reprodução completa da música antes de encerrar o pygame
pygame.quit()
