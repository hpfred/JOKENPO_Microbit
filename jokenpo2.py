from microbit import *
#import random

opcoes = ["pedra","papel","tesoura"] 
jokenpo = 0

while True:
#'''
    tesoura = Image('90009:09090:00900:09090:90009')  #X
    pedra = Image("09990:90009:90009:90009:09990")      #O
    papel = Image.SQUARE_SMALL
    P1 = Image('00900:09900:00900:00900:09990')
    P2 = Image('09990:00009:00990:09000:09999')
    tie = Image('00000:99999:00900:00900:00900')


#------------------------------------------------------Player1-----------------------------------
    jokenpo = 0
    while button_b.was_pressed() == False:
        if(button_a.was_pressed()):
            jokenpo += 1
        if (jokenpo > 2):
            jokenpo = 0
            
        if (jokenpo == 0):
            escolhido_player1 = "pedra"
            display.show(pedra)
        if (jokenpo == 1):
            escolhido_player1 = "papel"
            display.show(papel)
        if (jokenpo == 2):
            escolhido_player1 = "tesoura"
            display.show(tesoura)
            
        #if accelerometer.was_gesture("shake"):
        #    break; 
    #'''
    while button_a.was_pressed() ==  False:
        displayClear = Image('00000:00000:00000:00000:00000')
        display.show(displayClear)
    
    
    #------------------------------------------------------Player2-----------------------------------
    jokenpo = 0
    #if accelerometer.was_gesture("shake"):
    while accelerometer.was_gesture("shake") == False:
        if(button_a.was_pressed()):
            jokenpo += 1
        if (jokenpo > 2):
            jokenpo = 0
            
        if (jokenpo == 0):
            escolhido_player2 = "pedra"
            display.show(pedra)
        if (jokenpo == 1):
            escolhido_player2 = "papel"
            display.show(papel)
        if (jokenpo == 2):
            escolhido_player2 = "tesoura"
            display.show(tesoura)
            
 #------------------------------------------Resultado---------------------------------------------           
            
    if(escolhido_player1 == "pedra"):
        if(escolhido_player2 == "tesoura"):
            display.show(P1)
        if(escolhido_player2 == "pedra"):
            display.show(tie)
        if(escolhido_player2 == "papel"):
            display.show(P2)
            
    if(escolhido_player1 == "papel"):
        if(escolhido_player2 == "tesoura"):
            display.show(P2)
        if(escolhido_player2 == "pedra"):
            display.show(P1)
        if(escolhido_player2 == "papel"):
            display.show(tie)
            
    if(escolhido_player1 == "tesoura"):
        if(escolhido_player2 == "tesoura"):
            display.show(tie)
        if(escolhido_player2 == "pedra"):
            display.show(P2)
        if(escolhido_player2 == "papel"):
            display.show(P1)
            
    sleep(2000)
    
    jokenpo = 0
    escolhido_player1 = ""
    escolhido_player2 = ""
'''
    . . x . .
    . x x . .
    . . x . .
    . . x . .
    . x x x .
    
    . x x x .
    . . . . x
    . . x x .
    . x . . .
    . x x x x
    
    . . . . .
    x x x x x
    . . x . .
    . . x . .
    . . x . .
 '''