#faça um programa em python que abra e reproduza o audio de arquivo mp3
'''from python_play.player import play_it
play_it('C:/Users/Marcela/Downloads/musica/flp.mp3.mp3')'''

#esse modo não funciona mais
'''import pygame
pygame.init()
pygame.mixer.music.load('flp.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''
#tb tem esse modo que funciona
import playsound
playsound.playsound('flp.mp3.mp3')
