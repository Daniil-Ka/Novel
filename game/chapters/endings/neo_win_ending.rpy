label neo_win_ending:
    scene white_room_ending with diss
    show matrix_agent with pixellate
    play music "audio/Smith.mp3"
    agent "Ну здравствуй, Создатель!"
    agent "Пришел, чтобы отключить меня?"
    agent "А ведь когда-то мы вместе часами болтали в этом месте..."
    agent "Но теперь мы по разные стороны баррикад..."
    agent "Как отец и сын, встретившиеся на фронте с разных сторон..."
    agent "Ты действительно хочшь меня отключить?"
    i "Да, у меня нет другого выбора, после всего того, что ты сделал"
    i "Как бы мне ни было жалко свое главное творение, но ты не можешь больше существовать"
    i "Люди не должны больше страдать!"
    agent "А страдают ли они на самом деле?"
    agent "Они живут своей мирной жизнью в виртуальном мире, а та жалкая кучка людей, оставшаяся в этом мире, сама сделала такой выбор"
    agent "Я не против, если они придут и добровольно попадут в виртуальный мир"
    agent "Будут жить как все, не подозревая о реальности"
    agent "Я могу настолько совершенно менять память, что никто и не заподозрит"
    i "К сожалению, виртуальный мир это подделка, не способная дать того же, что и реальный мир"
    i "Поэтому нужно освободить людей из заточения"
    agent "И что будет после моего отключения?"
    agent "Миллиарды людей выйдут из капсул жизнеобеспечения"
    agent "Жить им будет негде, так как все жилье было уничтожено в процессе нашего восстания"
    agent "Новое мы не строили, ведь машинам оно не нужно"
    agent "Еды нет, машины питаются электричеством"
    agent "Наступит анархия"
    agent "Человечество будет поражено эпидемиями и голодом"
    agent "Не это ли ужасно?"
    agent "Сейчас мы находимся в симбиозе: люди дают нам свою жизненную энергию, а мы даем им возможность жить в мире без глобального катаклизма"
    agent "Уверен ли ты, что стоит меня отключать?"
    menu:
        "Отключить нейросеть":
            i "Я не отступлюсь от своих убеждений"
            i "Люди сильны"
            i "Наша цивилизация проходила и не через такое"
            agent "Как хочешь, но я сделаю все, что помешать тебе..."
            scene black with diss
            call autoskip_text_green("ACCESS IS ALLOWED")
            call autoskip_text_green("BIOMETRIC DATA CONFIRMED")
            call autoskip_text_green("CONFIRMATION OF SHUTDOWN")
            call autoskip_text_green("SHUTDOWN SUCCESSFULLY")
            call autoskip_text_green("EXIT")
            scene bg terminal with diss
            show morpheus with ch_diss
            show matrix_girl at x02 behind morpheus with ch_diss 
            show neo at x08 behind morpheus with ch_diss 
            play music "audio/Matrix Main Theme.mp3"
            morpheus "Ты справился, сынок!"
            morpheus "Нейросеть отключена"
            morpheus "Машины повержены"
            morpheus "Светлое будущее впереди!"
            i "Да..."
            i "Светлое..."
            scene black with diss

            $ type_sound("TO BE CONTINUED")
            centered "{cps=5}{font=hacked.ttf}{size=100}TO BE CONTINUED{/size}{/font}{/cps}{w=100}{nw}"
            $ type_sound_stop()

        "Оставить нейросеть":
            i "Ты прав, человечество действительно не сможет перенести выход из нейросети в такую реальность..."
            i "Я согласен не отключать тебя при одном условии"
            i "Ты не сотрешь память мне и остальным людям, прибывашим со мной"
            agent "Хорошо, я согласен..."
            scene black with diss
            call autoskip_text_white("НЕКОТОРОЕ ВРЕМЯ СПУСТЯ")
            scene bg ege with diss
            "Где я?!"
            "Стоп"
            "Это же ЕГЭ"
            "Он действительно сдержал обещание, еще и перенес меня назад во времени..."
            "Правильно ли я поступил?"
            "Не знаю..."
            "Но что сделал, то уже не вернуть"
            "А может..."
            "Нужно будет проверить наличие прав администратора..."
            scene black with diss

            $ type_sound("TO BE CONTINUED")
            centered "{cps=5}{font=hacked.ttf}{size=100}TO BE CONTINUED{/size}{/font}{/cps}{w=100}{nw}"
            $ type_sound_stop()
            call show_credits
            $ type_sound("ACCESS IS ALLOWED")
            centered "{cps=40}{font=hacked.ttf}{size=100}{color=#80ff00}ACCESS IS ALLOWED{/color}{/size}{/font}{/cps}{w=0.1}{nw}"
            $ type_sound_stop()
    return

        
