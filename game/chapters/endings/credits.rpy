init:
    transform credits:
        yalign 0
        linear 10 yalign 1

label show_credits:
    scene black with dissolve
    #show text "{font=hacked.ttf}{size=30}Работали над игрой:{p}{p}Аверьянов Максим - Разработчик, геймдизайнер{p}{p}Белоцерковский Кирилл - Тимлид, геймдизайнер{p}{p}Крапивин Даниил - Главный разработчик{p}{p}Кабак Максим - Дизайнер, Аналитик{p}{p}Першукова Анастасия - Дизайнер{/font}{/size}" at credits
    show text "dsadsada" at credits
    pause 40
    return
