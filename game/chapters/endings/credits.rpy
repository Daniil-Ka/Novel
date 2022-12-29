init:
    transform credits:
        yalign 1.5
        linear 40 yalign -1.5

label show_credits:
    scene black with dissolve
    play music "audio/Matrix Credits.mp3"
    show text "{font=hacked.ttf}{size=30}Работали над игрой:{p}{p}Аверьянов Максим - Разработчик, геймдизайнер{p}{p}Белоцерковский Кирилл - Тимлид, геймдизайнер{p}{p}Крапивин Даниил - Главный разработчик{p}{p}Кабак Максим - Дизайнер, Аналитик{p}{p}Першукова Анастасия - Дизайнер{p}{p}{p}{p}Использованная музыка:{p}{p}Red Alert 3 OST - Soviet March{p}{p}The Matrix OST - Clubbed to Death (Alina Gingertail Cover){/font}{/size}" at credits
    pause 40
