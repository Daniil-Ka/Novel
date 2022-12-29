define sounds = ['audio/Typewriter/v1.ogg', 'audio/Typewriter/v2.ogg', 'audio/Typewriter/v3.ogg', 'audio/Typewriter/v4.ogg', 'audio/Typewriter/v5.ogg']
define typewriter = u'typewriter'

init python:
    renpy.music.register_channel(typewriter, "sfx")

    def type_sound(text):
        renpy.sound.play(renpy.random.choice(sounds), channel=typewriter)
        for _ in range(len(text) // 5):
            renpy.sound.queue(renpy.random.choice(sounds), channel=typewriter)

    def type_sound_stop():
        renpy.sound.stop(channel=typewriter)

#ЗАСТАВКИ
label autoskip_text_colored(text, text_color):
    stop music
    $ type_sound(text)
    centered "{cps=15}{font=hacked.ttf}{size=100}{color=[text_color]}[text]{/color}{/size}{/font}{/cps}{w=1.0}{nw}"
    $ type_sound_stop()
    return

label autoskip_text_green(text):
    call autoskip_text_colored(text, "#80ff00")
    return

label autoskip_text_white(text):
    call autoskip_text_colored(text, "#fff")
    return 

label autoskip_text_red(text):
    call autoskip_text_colored(text, "#f00")
    return 