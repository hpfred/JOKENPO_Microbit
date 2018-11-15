# Escreva o seu código aqui :-)
from microbit import *
import random

opcoes = ["pedra","papel","tesoura"] 

jokenpo = 0

while True:
#'''
    tesoura = Image('90009:09090:00900:09090:90009')  #X
    pedra = Image("09990:90009:90009:90009:09990")      #O
    papel = Image.SQUARE_SMALL
  
    while accelerometer.is_gesture("shake") == False:
        if(button_a.was_pressed()):
            jokenpo += 1
        if (jokenpo > 2):
            jokenpo = 0
            
        if (jokenpo == 0):
            escolhido_player = "pedra"
            display.show(pedra)
        if (jokenpo == 1):
            escolhido_player = "papel"
            display.show(papel)
        if (jokenpo == 2):
            escolhido_player = "tesoura"
            display.show(tesoura)
            
        #if accelerometer.was_gesture("shake"):
        #    break; 
    #'''

    if accelerometer.was_gesture("shake"):
        escolhido = random.choice(opcoes)
        #display.scroll(escolhido)
        if(escolhido == "pedra"):
            display.show(pedra)
            sleep(2000)
        elif(escolhido == "papel"):
            display.show(papel)
            sleep(2000)
        elif(escolhido == "tesoura"):
            display.show(tesoura)
            sleep(2000)
            
    if(escolhido_player == "pedra"):
        if(escolhido == "tesoura"):
            display.show(Image.HAPPY)
        if(escolhido == "pedra"):
            display.show(Image.MEH)
        if(escolhido == "papel"):
            display.show(Image.SAD)
            
    if(escolhido_player == "papel"):
        if(escolhido == "tesoura"):
            display.show(Image.SAD)
        if(escolhido == "pedra"):
            display.show(Image.HAPPY)
        if(escolhido == "papel"):
            display.show(Image.MEH)
            
    if(escolhido_player == "tesoura"):
        if(escolhido == "tesoura"):
            display.show(Image.MEH)
        if(escolhido == "pedra"):
            display.show(Image.SAD)
        if(escolhido == "papel"):
            display.show(Image.HAPPY)
            
    sleep(500)