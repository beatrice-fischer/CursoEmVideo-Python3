# EXERCÍCIO 21 - abra e reproduza um áudio mp3

import pygame #biblioteca de jogos

pygame.init() #inicia
pygame.mixer.music.load('bambam_ribbon.mp3') #carrega a música
pygame.mixer.music.play() #inicia a música
pygame.event.wait() #espera a música terminar para encerrar
