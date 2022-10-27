# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define i = Character('Я', color='#c8ffc8')
define noname = Character('???', color='#fff7c8')

label start:
    call introdaction
    return
# todo