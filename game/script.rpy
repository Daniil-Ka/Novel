# Определение персонажей игры.
define i = Character('Я', color='#d3fd2a')
define noname = Character('???', color='#fff7c8')
define m = Character('Мамочка', color='#40ca40')
define anton = Character("Антон", color = '#eaaf19ff')
define teacher1 = Character("*учитель1*")
define teacher2 = Character("*учитель2*")
define teacher3 = Character("*учитель3*")
define sil1 = Character("Силуэт 1")
define sil2 = Character("Силуэт 2")
define morpheus = Character("Морфеус")
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