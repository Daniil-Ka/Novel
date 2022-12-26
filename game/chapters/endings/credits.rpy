init:
    transform credits:
        yalign 1.5
        linear 30.0 yalign -1.5

label show_credits:
    scene black with dissolve
    show text "{font=hacked.ttf}{size=30}Работали над игрой:{p}{p}Аверьянов Максим - Разработчик, геймдизайнер{p}{p}Белоцерковский Кирилл - Тимлид, геймдизайнер{p}{p}Крапивин Даниил - Главный разработчик{p}{p}Кабак Максим - Дизайнер, Аналитик{p}{p}Першукова Анастасия - Дизайнер{/font}{/size}" at credits
    pause 30
    return