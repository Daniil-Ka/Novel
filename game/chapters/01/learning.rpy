label learning_start:
    define math_teacher = Character('Чуксина', color='#ff0000')
    call .choice_subjects
    call .start_of_learning
    call .math_lesson
    call .dream
    call .math_test
    return

label .choice_subjects:
    show bg choice_subjects with diss
    "Звонок будильника, пора вставать"
    "Сегодня важный день! Вчера наставники рассказали, что сегодня день выбора предметов!"
    "Нужно постараться и успеть выбрать нужные курсы и удобное расписание, иначе придется ждать еще семестр до следующей смены расписания"
    return

label .start_of_learning:
    scene bg urfu rtf holl with diss
    "Дни мелькали один за другим"
    "Я познакомился с преподавателями"
    "Сходил на различные мероприятия"
    "Получил первую стипендию!"
    "Наша группа выступила на дебюте первокурсников"
    "Я постепенно вливался в ритм студенческой жизни"
    "Как выяснилось, время на учебу найдется всегда, даже если у тебя за день 5 мероприятий"
    "В общем, все происходящее в разы превосходило мои ожидания"
    return

label .math_lesson:
    scene bg math_class with diss
    "В очередной раз придя на пару по математике я услышал страшные для любого ученика слова:"
    math_teacher "На следующей паре у нас будет контрольная работа сразу по нескольким темам!"
    math_teacher "Кто не придет или опоздает, того на пересдачу не пущу!"
    "В этот момент все в моей груди сжалось"
    "Я совершенно не понял последние две темы, а среди моих знакомых нет хороших математиков"
    "Придется все учить по видео в интернете, но тогда мне явно не хватит двух дней до следующей пары"
    "Что же делать..."
    "Из раздумий меня вывел вновь прозвучавший голос преподавателя"
    math_teacher "На сегодня все, можете быть свободны"
    "Я вышел из класса и побрел в сторону буфета, намереваясь заглушить свое горе парой бутербродов из тогрового автомата"
    scene bg urfu rtf holl with diss
    "Уже на подходе к буфету я вспомнил, что оставил в аудитории свою куртку, и нужно поторопиться, чтобы не искать потом ключи от замка"
    "Я так торопился, что не заметил открывающейся двери и столкнулся головами с выходящим человеком"
    "Перед тем как потерять сознание, я понял, что это был мой преподаватель"
    scene black with diss
    "Голова налилась свинцом и я отключился"
    return

label .dream:
    scene bg teacher_home with diss
    "Странно, раньше я не видел такой аудитории в институте"
    "Все выглядит по-домашнему, тепло и уютно"
    "За столом сидит *Препод name* и что-то пишет на листочках"
    "Наверное, проверяет чьи-то работы, или готовит контрольную"
    "Контрольную..."
    "СТОП"
    "Это же не аудитория, а квартира *препод*!"
    "Но как я сюда попал?! Я только что был в институте"
    "Что происходит!"
    "Это игра моего сознания? Сон? Параллельная реальность?"
    "Я не понимаю, что происходит!"
    "Точно, я же столкнулся с ней рядом с аудиторией!"
    "Но это ничего не объясняет, как я оказался у неё дома?!"
    "Может, я впал в кому, или это осознанное сновидение в отключке?"
    menu:
        "Привлечь внимание преподавателя?"
        "Да!":
            call .interfere_in_conversation

        "Лучше понаблюдать.":
            call .not_interfere_in_conversation
    return

label .interfere_in_conversation:
    "Нужно спросить что-то нейтральное, вдруг я не пришел в себя и не осознаю реальность"
    show math teacher with ch_diss
    i "Препод_нэйм, извините, вы сейчас пишете нам задания на контрольную?"
    math_teacher "Да"
    "Она ответила и вернулась к своим записям"
    i "*Препод*, вы не перенесете проверочную на следующую пару?"
    i "Возникла такая ситуация, что я не очень понял последние две темы, и просто не успею их пройти за два дня"
    math_teacher "Я не буду ради тебя одного переносить контрольную, у меня итак на следующей неделе дел по горло!"
    #TODO: сделать условие
    $condition = False
    menu:
        "Как уговорить преподавателя?"
        "Надаваить на жалость":
            i "Но я не один не понял тему! Многие мои одногруппники тоже не смогли в ней разобраться, а вы уже даете контрольную работу!"
            math_teacher "Это не мои проблемы, не пытайся давить мне на жалость!"
            math_teacher "Если человек не смог понять математику, то он не достоин гордого звания программиста!"
            math_teacher "На работе тебя никто жалеть и ждать не будет, так что я делаю только лучше, развеивая ложные ожидания"
            i "Но почему вы так категоричны?! Вы можете сломать жизнь человеку, если его из-за вас отчислят!"
            show math teacher angry with ch_diss
            math_teacher "Да на моем веку этих отчисленных уже пруд пруди, одним больше, одним меньше"
            math_teacher "У меня есть дела поважнее, спасение утопающих - дело рук самих утопающих"
            math_teacher "На следующей неделе у меня юбилей и мне некогда будет заниматься контрольными"
            math_teacher "Как ты вообще попал в мою квартиру?! Пошел вон отсюда!"
            scene black with diss
            "Я погрузился во мрак и снова потерял сознание"

        "Уговорить":    
            $condition = True
            #TODO

    scene bg urfu rtf holl with diss                
    "Наконец, я очнулся. Странный был сон, но вроде бы теперь все в порядке"
    "Я посмотрел на учительницу лежащую рядом"
    "*Препод* тоже приходила в сознание"
    show math teacher with ch_diss
    "Она очень странно на меня посмотрела"
    i "Извините пожалуйста. Моя куртка осталась в аудитории."
    "Она молча открыла кабинет и я забрал куртку."
    if not condition:
        "В её ледяном взгляде чувствовалось подозрение и тонкая нотка злости"
    "Но, тем не менее, мы ничего друг другу не сказали и разошлись, когда я забрал куртку"
    "Это был всего лишь сон..."
    "Я одел куртку и вышел на улицу" 
    scene bg 1st_september with diss
    "Осенний воздух приятно обдувал лицо, пока я шел в сторону дома"
    "Странный силуэт мелькнул в толпе..."
    scene bg home with diss
    "Я дошел до дома и начал думать, что делать дальше"
    "Можно начать готовиться к контрольной, наверное, это самое полезное, что я сейчас могу сделать"
    "Но голова начала так сильно болеть и я решил лечь спать"
    "Сон - лучшее лекарство"
    scene black with diss
    "Несколько дней спустя..."

    return

label .not_interfere_in_conversation:
    $is_have_answers = False
    show bg teacher_home_cabinet with diss
    "Простояв на месте несколько минут, вы решаете заглянуть в другую комнату."
    "Посреди комнаты стоит стол, на котором лежат бумаги."
    "Подойдя, вы понимаете, что это ответы на контрольную работу."
    "Вы быстро списываете ответы (кууууууда?) и прячитесь в шкафу."

    "Через некоторое время он там засыпает и оказывается в больнице"
    "Он понимает, что попал каким-то образом в сон математички, но не понимает как."
    "Его выписывают из больницы, он возвращается домой, он понимает, что вещи он переносить из сна в сон не может. Он засыпает... "

    "Он оказывается в своем сне, и понимает, что те действия которые он совершает в чужих снах, косвенно оказывается в его сне, то есть тот листок который он сделал во сне математички оказался у него во сне на столе."
    
    "Он пытается это перенести во сне в свой компьютер, поднимается сутра и видит, что файл действительно у него на рабочем столе, он его распечаетывает и идет в универстиет."

    "Так как он не вмешивался в процесс и во сне математички он не было замечен, то его математичка не помнит."

    "Он пишет контрольную без проблем и получает максимальный балл."

    "Он пишет контрольную без проблем и получает максимальный балл."

    "Он понимает, что может воровать идеи и мысли у других людей, он решает сохранить в тайне данную способность, потому что он боится, что если об этом узнают то его будут пытать."

    "Он пытается понять как использовать эту возможность, пытается незаметно проникнуть в сны разных людей."

    menu:
        "Он понимает что никогда не видел своего отца, и пытается подумать о нем перед сном, чтобы узнать побольше о нем"

        "Попасть в сон отца":
            "Пытается попасть в сон отца и у него неполучается"

            "он видит только темный силуэт во сне, просыпаясь он понимает, что он не видит сон своего отца, но не понимает почему"

            "пока он спит, происходит темная сценка, где все кричат, мы его засекли"

            "вторая сценка, силуэт сидит и плачет от радости"

            "Просыпаясь ГГ решает учувствовать в хакатоне по разработке нейросети, ведь он обладает, сверхспособностью"

            "Он собирает команду, в истечению первого дня он видит как сильный игрок противоположной команды засыпает и он решает попасть в его сон, он видит все его идеи и сомещая со своими создает лучшую нейросеть прогнозирующую продолжительность жизни людей"

            "Он выигрывает хакатон и и идет домой радостный и его сбивает машина"

        "Не поподать в сон отца":
            "Боится делать шаг в неизвестность"

            "Он учавствет в олимпиаде и пробравшись в сон к организатору видит все  ответы, занимает первое место и получает большой грант"

            "Он решает учувствовать еще и в хакатоне, ведь у него сверхспособность"

            "Он собирает команду, в истечению первого дня он видит как сильный игрок противоположной команды засыпает и он решает попасть в его сон, он видит все его идеи и сомещая со своими создает лучшую нейросеть прогнозирующую продолжительность жизни людей"

            "Подумав, он решает все таки попасть в сон к отцу"

            "он видит только темный силуэт во сне, просыпаясь он понимает, что он не видит сон своего отца, но не понимает почему"

            "пока он спит, происходит темная сценка, где все кричат, мы его засекли"

            "вторая сценка, силуэт сидит и плачет от радости"


    return

label .math_test:
    scene bg math_class with diss
    "\"Долгожданный\" день настал. Сегодня придется писать контрольную, а я так и не смог к ней подготовиться"
    #Вмешался, кр перенесли
    if condition: 
        call matrix_win
    #Не вмешался, достал ответы
    elif is_have_answers:
        call neo_win
        #TODO
        #Прописать то, что гг не вмешался в сон и попытался достать ответы на контрольную (+пару выборов во всне)
        
    #Не вмешался и не достал ответы либо не получилось перенести кр
    else:
        "Надо решать задачи, а в голове только перекати-поля не хватает"
        "И почему нигде нет ответов на эту контрольную? Видимо она составила её сама."
        "В лучшем случае останусь без стипендии, а в худшем..."
        scene black with diss
        "Следующая пара матанализа"
        scene bg math_class with diss
        show math teacher with ch_diss
        math_teacher "Астапов Антон- 3"
        "Ну, уже не двойка."
        math_teacher "Осипов Владимир- 2"
        "Жаль, конечно, этого добряка..."
        math_teacher "Абрамов Святослав- 5"
        "Везет кому-то, мне на такое и надеяться не стоит"
        math_teacher "Артемова Анастасия - 4"
        "Эх, она оказывается еще и умная..."
        math_teacher "*фамилия игрока* - 2, хотя, будь моя воля, я бы поставила кол"
        "Да-а-а, вот же, придется к ней на отработку идти, чтобы без стипендии не остаться"
        call data_science_ending
    return
