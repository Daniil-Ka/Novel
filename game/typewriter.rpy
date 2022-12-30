define sounds = ['audio/Typewriter/v1.ogg', 'audio/Typewriter/v2.ogg', 'audio/Typewriter/v3.ogg', 'audio/Typewriter/v4.ogg', 'audio/Typewriter/v5.ogg']
define typewriter = u'typewriter'

init python:
    renpy.music.register_channel(typewriter, "sfx")

    def change_music(name):
        name = "audio/" + name + ".mp3"
        renpy.play(name, channel = "music", fadeout = 1, fadein = 1)

    def type_sound(text):
        renpy.sound.play(renpy.random.choice(sounds), channel=typewriter)
        for _ in range(len(text) // 5):
            renpy.sound.queue(renpy.random.choice(sounds), channel=typewriter)

    def type_sound_stop():
        renpy.sound.stop(channel=typewriter)

#ЗАСТАВКИ
label autoskip_text_colored(text, text_color):
    $c = renpy.audio.audio.get_channel("music")
    $renpy.music.set_volume(0, delay = 0.5, channel = "music")
    pause 0.5
    $c.pause()
    $type_sound(text)
    centered "{cps=15}{font=hacked.ttf}{size=100}{color=[text_color]}[text]{/color}{/size}{/font}{/cps}{w=1.0}{nw}"
    $type_sound_stop()
    $c.unpause()
    $renpy.music.set_volume(1, delay = 5, channel = "music")
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