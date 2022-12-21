label matrix_win:
    show math teacher with ch_diss
    "*Препод* странно взглянула на меня и сказала:"
    math_teacher "Я чувствую, что вы еще не совсем готовы к контрольной, поэтому на сегодняшней паре мы с вами повторим материал"
    hide math teacher
    "Что?"
    "Это совпадение? Не думаю"
    "Слишком уж странно она на меня посмотрела, да и такие фокусы, по рассказам второкурсников, не в её стиле"
    "Остаток пары прошел в обычном формате. Мы повторяли тему и я наконец разобрался в задачах"
    scene bg urfu rtf holl with diss
    "После пары я отправился домой, чтобы вечером проверить одну теорию..."
    scene black with diss
    "Несколько часов спустя..."
    scene bg home night with diss
    "Я весь день думал над произошедшим"
    "Правда ли я могу попадать в чужие сны? Если это так, то что мне нужно для это сделать?"
    "Эксперимент №0 - попытка сосредоточиться на мысялх о целевом объекте"
    "Я попытаюсь проникнуть в сон к Антону, моему другу, с которым мы завтра встретимся на парах"
    "Я сосредоточился на мыслях о нем и уснул"
    scene bg summer 2 with diss
    "Проснулся я уже стоя на волейбольной площадке рядом с другом"
    "Мы играли в пляжный волейбол два на два"
    show friend_anton with ch_diss
    anton "Подавай, твоя очередь!"
    i "Сейчас я им такую подачу навешаю!"
    "Я подкинул мяч и ударил со всей силы"
    "Мяч отскочил от руки и полетел прямиком Антону в лицо"
    "Антон упал от полученного удара"
    scene black with diss
    "После этих слов что-то невидимое вытащило меня из сна"
    "Это был будильник"
    scene bg home with diss
    "Пора идти на пары, там нужно будет постараться узнать от Антона о его сне"
    scene bg urfu rtf holl with diss
    show friend_anton with ch_diss
    anton "Привет, давно не виделись!"
    i "Привет, и в правду давно"
    "Я взглянул на часы"
    i "Целых 16 часов!"
    anton "Представляешь, мне тут такой сон приснился!"
    anton "С самого утра не могу дождаться, чтобы рассказать тебе"
    anton "Летом я каждый день ходил играть в волейбол на местный пляж, а сегодня мне приснилось, что мы играем вместе, представляешь!"
    anton "При этом, такого не могло быть ни при каком раскладе, ведь тогда мы еще не были знакомы"
    anton "Ты должен был подавать и хвастался, что сейчас точно забъешь"
    anton "Забить то ты забил, да вот только не в поле, а мне в лицо"
    anton "Даже сейчас голова раскалывается, будто и не спал вовсе"
    hide friend_anton
    "Дальше я уже ничего не слышал"
    "Я был настолько поражен тем, что действительно могу попадать в чужие сны."
    "Но есть один нюанс, в таком случае, люди могут меня запомнить и заподозрить что-то неладное."
    "Но такими возможностями не разбрасываются, поэтому нужно её использовать по максимуму."
    "Сегодня ночью нужно обязательно попробовать проникнуть в сон к кому-то еще."
    scene bg home night with diss
    "Итак, выбираем кандидата."
    "К кому бы попробовать проникнуть?"
    "Точно! У меня же завтра контрольная по английскому."
    "Вот и новый кандидат для следующей попытки."
    scene black with diss 
    "Месяц спустя. Преподавательская."
    scene bg teachers_room with diss
    show teacher1 at x03 with ch_diss
    show teacher2 at x05 with ch_diss
    show teacher3 at x07 with ch_diss
    teacher1 "teacher2, ты чего такая задумчивая?"
    teacher2 "Да вот, странно как-то, что ни контрольная, так снится мне один студент."
    teacher2 "И, что самое интересное, после этого всегда пишет контрольную на максимальный балл"
    teacher1 "А это, случаем, не player_name?"
    teacher2 "Да, откуда ты узнала? Он тебе что, тоже снится?"
    teacher1 "Да, абсолютно такая-же ситуация!"
    teacher3 "Представляете, мне тоже! Как-то странно все это..."
    teacher1 "И в правду..."
    scene black with diss
    "Где-то в другом месте..."
    scene bg black_matrix_silhuette with Dissolve(4, time => 0 if time < 3 else time - 3)
    scene bg black_matrix_silhuette_2 with Dissolve(2.0)
    sil1 "Мы наконец-то его обнаружили."
    sil2 "Верно."
    sil1 "Нам стоит его прикончить."
    sil2 "Верно"
    sil1 "Он можен принести нам много вреда."
    sil2 "Верно"
    sil1 "Тогда пора действовать."
    sil2 "Верно"

    #TODO Схватка ИИ и Сопротивления, слайдшоу или что я хз
    #ГГ общается в сопротивлением

    call matrix_story
    morpheus "Верить или не верить, решать тебе. Но если ты останешься в этом мире, то вскоре тебя настигнет нейросеть и все начнется сначала"
    morpheus "По-хорошему я мог бы предложить тебе выбрать синюю или красную таблетку"
    morpheus "Но нам очень нужны твои знания, а если ты останешься здесь, то мы снова тебя потеряем"
    morpheus "Так что у тебя нет выбора кроме как пойти с нами и спасти жителей этого мира"
    i "Хорошо, я согласен пойти с вами"
    #TODO
    #Врывается ИИ и убивает половину команды
    #Слайды
    "Вдруг меня оглушил взрыв"
    "В комнате поднялась пыль и ворвались десятки клонов"
    "Единственное, что я успел сделать - это схватить красную таблетку и проглотить её"
    scene black with diss
    "Сознание помутнилось и я отключился"
    call red_pill

    scene bg riot_ship with diss
    show morpheus with ch_diss
    morpheus "Я давно думал над тем, как отключить нейросеть."
    morpheus "На основе твоих записей я составил план"
    morpheus "Но мы не могли воплотить его в жизнь без тебя"
    morpheus "Точнее без твоей способности проникать во сны..."
    morpheus "Как ты уже в курсе, нейросеть максимально близка к человеческому сознанию"
    morpheus "Во время эволюции нейросеть получила возможность видеть сны"
    morpheus "Войдя в сон нейросети мы должны проникнуть на второй уровень сновидений, т.е. в её подсознание"
    morpheus "Оттуда мы сможем деактивировать нейросеть и захватить управление всеми роботами в мире"
    i "Я согласен с твоим планом, но есть один нюанс"
    i "Когда я в прошлый раз пытался победить нейросеть, я не успел воспользоваться эффектом неожиданности и меня засекли"
    i "На меня напали десятки клонов нейросети и я не успел выйти из программы"
    i "Поэтому, если мы не хотим проиграть в этой войне, нужно быстро и дерзко проникнуть в сон нейросети, где мы будем в относительной безопасности"
    morpheus "На этот вариант у меня есть идея"
    morpheus "Отправим пару людей напрямую для отвлечения внимания, и пока нейросеть будет занята устранением угрозы, мы проникнем в её сон"
    i "Хорошо, когда приступим?"
    morpheus "Теперь, когда у нас есть все необходимое, нам осталось только дождаться твоего полного восстановления"
    morpheus "А затем мы приведем наш план в действие и наконец отключим эту нейросеть!"
    scene black with diss
    "Две недели я упорно тренировался и восстанваливал свои навыки."
    scene bg riot_ship with diss
    show morpheus with ch_diss
    morpheus "Ну что, времени ждать больше нет. Придется действовать теми силами, что имеются в наличии. нейросеть уже начала подозревать о нашем плане"
    