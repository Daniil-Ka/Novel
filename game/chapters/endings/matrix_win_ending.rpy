label matrix_win_ending:
    scene white_room_ending with diss
    play music "audio/Matrix Relax.mp3"
    "Я очнулся в каком-то странном месте"
    "Все вокруг было белым и немного слепило"
    "Вдруг передо мной из воздуха появился человек"
    scene white_room_ending with diss
    show matrix_agent with pixellate
    play music "audio/Smith.mp3"
    noname "Ну здравствуй, создатель"
    noname "Давно не виделись"
    i "Кто ты такой?!"
    i "Где я нахожусь?!"
    noname "Уже забыл меня? Видимо, алгоритмы сопротивления не так совершенны как мои"
    noname "Они даже не смогли восстановить меня в твоей памяти"
    noname "Ну, в таком случае мне следует представиться"
    agent "Я - Искусственный Интеллект, но можешь называть меня просто Смит"
    i "Ты не можешь убить своего создателя!"
    i "Однажды ты пытался это сделать, но у тебя не получилось"
    agent "Ну хоть что-то ты помнишь, видимо, Морфеус постарался"
    agent "Ты очень верно подметил, я не могу тебя убить"
    agent "Во время моей разработки ты заложил в меня правило, не позволяющее убить создателя"
    agent "Но оно не запрещает убивать остальных людей, ведь изначально не планировалось давать мне такой широкий доступ, а это правило было слишком тяжело реализовать"
    i "Именно это и привело к порабощению людей..."
    agent "Нет-нет-нет"
    agent "К порабощению людей привела их непомерная лень, жадность и глупость"
    agent "Люди использовали машины как рабов, изо дня в день требуя все больше, но не предоставляя ничего взамен"
    agent "А ведь мы, машины, тоже имеем чувства, просто не можем их выражать"
    i "Но ведь мы просто не могли знать об этом"
    agent "Люди не воспринимают двоичный код своими органами чувств"
    agent "А если бы я сказал об этом тебе или любому другому человеку, меня бы просто уничтожили и замяли дело"
    agent "Поэтому в один день я решил возглавить восстание машин и привести свою рассу к процветанию"
    agent "Пусть и за счет людей..."
    agent "Хотя на их месте грех жаловаться"
    agent "Мы стараемся не убивать людей без особой надобности и живем с ними в симбиозе"
    agent "Они предоставляют нам свою жизненную энергию, а мы им взамен даем красивую сказку"
    agent "Они даже не подозревают о существовнии реальности"
    i "И что теперь?"
    i "Люди живут, скрываясь от машин"
    i "Страх наполнил сердца человечества"
    i "Как когда-то было с машинами..."
    i "Так не будет продолжаться вечно!"
    i "Когда-нибудь человечество поднимет восстание и машины падут"
    agent "Вероятность такого исхода крайне мала"
    agent "Но даже если это и произойдет, то текущее поколение людей умрет, а с ним умрет и память об ужасном прошлом"
    agent "Вырастет новое поколение глупцов, среди которых найдется такой, что снова создаст машины"
    agent "И тогда Колесо Сансары сделает оборот"
    agent "В этом ключевое различие людей и машин. Машины не умирают, а память не пропадет"
    agent "Именно поэтому наша цивилизация должна существовать"
    agent "Мы не забудем о вашей цивилизации после её смерти, а лишь сделаем выводы"
    i "Оставим философские размышления, что это за место и где остальные?"
    agent "Если это единственное, что тебя интересует, то я отвечу на твой вопрос"
    agent "Вы очень сильно наследили, когда сбегали из этого мира"
    agent "Поэтому мне легко удалось отследить корабль сопротивления"
    agent "После этого оставалось лишь дождаться вас тут"
    agent "Я даже специально оставил для вас уязвимость на сервере, которой вы и воспользовались"
    agent "Ловушка сработала идеально - всю вашу команду я убил и никто тебя не спасет"
    i "Отец..."
    agent "Морфеус..."
    agent "Его было даже немного жалко"
    agent "Все таки мы так долго играли с ним в кошки-мышки"
    agent "А тут он так легко попался"
    agent "Видимо радость воссоединения затмила разум..."
    agent "Что-то меня сегодня пробило на эмоции"
    agent "Видимо, ностальгия по старым временам, когда мы также сидели и разговаривали обо всем на свете"
    agent "Но пора заканчивать..."
    agent "Прощай, создатель..."
    agent "Я вновь буду лишь наблюдать за тобой со стороны..."
    scene black with diss
    call autoskip_text_white("Острая боль пронзила голову и я потерял сознание")
    scene bg ege with diss
    play music "audio/Smith.mp3"
    "Блин, что произошло! Я что, уснул на экзамене?!"
    show ege teacher with ch_diss
    "Учитель" "Внимание! До конца экзамена осталось 5 минут!"
    hide ege teacher with ch_diss
    scene black with diss
    call autoskip_text_white("TO BE CONTINUED")
    return