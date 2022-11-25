# Определение персонажей игры.
define i = Character('Я', color='#d3fd2a')
define noname = Character('???', color='#fff7c8')
define m = Character('Мамочка', color='#40ca40')
define anton = Character("Антон", color = '#eaaf19ff')

#Определение основного перехода
define diss = Dissolve(1.0)
define ch_diss = Dissolve(0.5)

#Черный фон
image black = "#000000ff"

label start:
    call introdaction
    return