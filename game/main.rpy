# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define i = Character('Я', color='#d3fd2a')
define noname = Character('???', color='#fff7c8')
define m = Character('Мамочка', color='#40ca40')

label start:
    call introdaction
    return
# todo