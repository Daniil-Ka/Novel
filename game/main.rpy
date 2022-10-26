# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define you = Character('Вы', color="#c8ffc8")
define noname = Character('???', color="#fff7c8")

label start:
    call introdaction
    return
