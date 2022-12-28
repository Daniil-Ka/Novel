# Определение персонажей игры.
define noname = Character('???', color='#bababa')
define m = Character('Мама', color='#ea00ff')
define anton = Character("Антон", color = '#421eceff')
define teacher1 = Character("Аркадий Петрович", color='#3d82ad')
define teacher2 = Character("Денис Борисович", color='#beeeb4')
define teacher3 = Character("Георгий Владимирович", color='#e1e48e')
define sil1 = Character("Силуэт 1", color='#ff0000')
define sil2 = Character("Силуэт 2", color='#ff0000')
define morpheus = Character("Морфеус", color='#9000ff')
define agent = Character("Смит", color='#00ff51')
define o = Character("Организатор хакатона", color='#ef9797')
define math_teacher = Character('Светлана Владимировна', color='#ff5100')

#Определение основного перехода
define diss = Dissolve(1.0)
define ch_diss = Dissolve(0.5)

#Анимированные спрайты
image matrix_agent:
    "smit"
    pause 1
    "glitch1"
    pause .1
    "smit"
    pause 1.2
    "glitch2"
    pause .1
    "smit"
    pause .3
    "glitch3"
    pause .1
    "smit"
    pause 1
    "glitch4"
    pause .1
    "smit"
    repeat
    

#Определение позиций
transform x01:
    yalign 1.0
    xalign 0.2

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

transform xt1:
    yalign 1.0
    xalign 0.05

transform xt2:
    yalign 1.0
    xalign 0.4

transform xt3:
    yalign 1.0
    xalign 0.95

#Черный фон
image black = "#000000ff"

# переопределение поля ввода
# $ renpy.input("Введите ваше имя:")
style input_style:
    font "hacked.ttf"
    xalign 0.5
    size 40

screen input:   
    window style "nvl_window":
        has vbox
        yalign 0.5
        xalign 0.5
        
        text prompt yalign 0.4 color "#80ff00" style "input_style"
        input id "input" yalign 0.5 color "#fff" style "input_style"

label start:
    python:
        name = renpy.input("Введите ваше имя:")
        name = name.strip() or "Шадрин Дата Бэйс"
    define i = Character("[name]", color='#40ca40')
    call introdaction
    return