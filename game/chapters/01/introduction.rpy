label introdaction:
    scene bg ege with diss
    "Вы проснулись и внезапно вспомнили, что находитесь на экзамене."
    show ege teacher with ch_diss
    "Учитель" "Внимание! До конца экзамена осталось 5 минут!"
    hide ege teacher with ch_diss
    "Всего 5 минут! Нужно скорее решить последнюю задачу."
    scene bg ege test with diss
    "Определите, при каких значениях параметра a уравнение имеет ровно два решения."
    menu:
        "Определите, при каких значениях параметра a уравнение имеет ровно два решения."
        "a < 0, a = e * ln2":
            "Успел!"
            "Остается только надеяться, что ответ получился правильный."
            scene bg home night with diss
            "Несколько бессонных ночей спустя..."
            i "Ура!!! 98 баллов по математике! Надо рассказать маме!"
            # scene разговор с матерью
            i "МАМА!!! У меня за ЕГЭ 98 баллов!!!"
            m "Молодец сынок! Я знала, что у тебя все получится!"
            i "Спасибо, что ты меня поддерживала весь этот год!"
            m "Можешь идти развлекаться. Ты это заслужил."
            call .admission_to_URFU
        "Эээ, не знаю":
            "Это действительно сложный параметр для меня."
            "Придется сдавать работу без этой задачи"
            scene bg home night with diss
            "После нескольких бесонных ночей в ожидании результатов..."
            call mobilization_ending
    return

label .admission_to_URFU:
    
    
    call .summer_slideshow
    scene bg urfu main with diss
    "Наконец, настал день подачи документов"
    "Баллы у меня достаточно высокие, поэтому и выбор неплохой"
    "Но, как известно, чем больше вариантов - тем сложнее выбрать один из них"
    menu:
        "Медлить больше нельзя, пора что-то выбрать"
        "ИРИТ-РТФ":
            "У меня там учился отец! Там же буду учиться и я!"
            "Да и говорят, что учиться тут легко и весело"
            "Какие-то командные проекты, игры делать нужно"
            "В любом случае это лучше, чем учить математику 24 часа в сутки, 7 дней в неделю"
            # todo
            scene black with diss
            "Некоторое время спустя..."
            scene bg 1st_september with diss
            "Наступает 1 сентября."
            i "Наконец-то пришло время! Увижу своих одногруппников, возможно даже подружусь с кем-то"
            "В потоке мероприятий день незаметно перешел в вечер"
            scene bg 1st_september evening with diss
            "Всех первокурсников распустили по домам готовиться к предстоящей учебе"
            scene bg home night with diss
            "Да-а-а, насыщенный был денёк. Столько меропреятий, и все в один день!"
            "Наставники говорят, в будущем мероприятий будет становиться только больше"
            "А некоторые из мероприятий даже самим придется организовывать"
            "Поступил учиться, называется!"
            "Ну, деваться уже некуда, придется как-то выкраивать среди всего этого время и на учебу, чтобы не отчислили на первой же сессии"
            scene black with diss
            "Я лег на кровать и моментально оказался в царстве Морфея, видимо, сказывается накопленная за день усталость"
            call learning_start
        "МатМех":
            "Некотрые мои друзья туда поступили."
            "Может попробывать поступить вместе с ними?"
            call expulsion_ending
    return

label .summer_slideshow:
    scene bg summer 1 with diss
    "Как же классно я веселился с друзьями! Я так рад, что обрел новые знакомства!"
    scene bg summer 1 with diss
    "Я был с родителями на море! Такие красивые пейзажи..."
    # scene пейзажи моря 2-3 штуки
    "Познакомился с девушкой! Она такая классная..."
    # scene с девушкой на мосту
    "Я ездил на рыбалку. Поймал огромную щуку!!!"
    # scene рыбалка в лодке
    "Это было классное лето..."
    scene bg home with diss
    return
