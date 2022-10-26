label introdaction:
    scene bg ege
    "Вы проснулись и внезапно вспомнили, что находитесь на экзамене."
    "Посмотрев на часы вы понимаете, что до конца ЕГЭ осталось 5 минут."
    "Вам осталось решить лишь одну задачу, чтоб точно сдать этот экзамен."
    scene bg ege test
    menu:
        "Определите, при каких значениях параметра a уравнение имеет ровно два решения."
        "a < 0, a = e * ln2":
            "В надежде на то, что ваш ответ правильный, вы сдаёте свою работу."
            call .admission_to_URFU
        "Эээ, не знаю":
            call mobilization_ending
    return   

label .admission_to_URFU:
    "После нескольких бесонных ночей в ожидании результатов..."
    "Получив высокий балл, вы задумались, на какое же направление поступать"
    call .summer_slideshow
    scene bg admission_to_URFU

    menu:
        "Конечно же ИРИТ-РТФ!":
            # todo
            show bg 1st_september
            "Наступает 1 сентября."
            "Впечатления?"
            
            "Кто этот ваш пасс-блок???"
            call learning_start
        "МатМех?":
            call expulsion_ending
    return

label .summer_slideshow:
    # $ renpy.movie_cutscene('.webm')
    return
