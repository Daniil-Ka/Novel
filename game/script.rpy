# Определение персонажей игры.
define i = Character('Я', color='#d3fd2a')
define noname = Character('???', color='#ffc8c8')
define m = Character('Мама', color='#40ca40')
define anton = Character("Антон", color = '#ff0000ff')
define teacher1 = Character("*учитель1*")
define teacher2 = Character("*учитель2*")
define teacher3 = Character("*учитель3*")
define sil1 = Character("Силуэт 1")
define sil2 = Character("Силуэт 2")
define morpheus = Character("Морфеус")
define agent = Character("Смит")
define o = Character("Организатор хакатона")
#Определение основного перехода
define diss = Dissolve(1.0)
define ch_diss = Dissolve(0.5)

#Определение позиций
transform x02:
    yalign 1.0
    xalign 0.2

transform x03:
    yalign 1.0
    xalign 0.3

transform x04:
    yalign 1.0
    xalign 0.4

transform x05:
    yalign 1.0
    xalign 0.5

transform x06:
    yalign 1.0
    xalign 0.6

transform x07:
    yalign 1.0
    xalign 0.7

transform x08:
    yalign 1.0
    xalign 0.8

#Черный фон
image black = "#000000ff"


label start:
    call introdaction
    return

#ЗАСТАВКИ
label autoskip_text_colored(text, text_color):
    centered "{cps=15}{font=hacked.ttf}{size=100}{color=[text_color]}[text]{/color}{/size}{/font}{/cps}{w=1.0}{nw}"
    return

label autoskip_text_green(text):
    call autoskip_text_colored(text, "#80ff00")
    return

label autoskip_text_white(text):
    call autoskip_text_colored(text, "#ffffff")
    return 

label autoskip_text_red(text):
    call autoskip_text_colored(text, "#ff0000")
    return 