label learning_start:
    show bg choice_subjects
    call .choice_subjects
    call .math_test
    return

label .choice_subjects:
    define math_teacher = Character('Чуксина', color='#ff0000')
    "Выбор предметов"
    return

label .math_test:
    show bg math_test
    "Вы приходите на контрольную по математике, при этом забыв к ней подготовиться."
    "Пытаясь решить хоть что-нибудь"

    #todo
    "многа воды..."
    call .dream
    return

label .dream:
    show bg teacher_home
    "Оказываетесь в доме учительницы."
    menu:
        "Вмешаться?"
        "ДА!":
            "Ваше присутствие замечают. Начинается диалог."

            i "Перенесёте проверочную?"
            if True:
                math_teacher "ХАХАХАХАХ. НЕТ."
                call expulsion_ending
            else:
                "Может быть."

        "Лучше понаблюдать.":
            show bg teacher_home_cabinet
            "Простояв на месте несколько минут, вы решаете заглянуть в 
            другую комнату."
            "Посреди комнаты стоит стол, на котором лежат бумаги."
            "Подойдя, вы понимаете, что это ответы на контрольную работу."
            "Вы быстро списываете ответы (кууууууда?) и прячитесь в шкафу."

            show bg hospital
            "Больница..."

    return