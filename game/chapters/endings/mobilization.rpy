label mobilization_ending:
    "3 балла за ЕГЭ... Я сделал слишком много ошибок..."
    "Это конец..."
    scene bg mobilization with diss
    $change_music("Mobilization")
    call ending("На следующий день вам пришла повестка...")
    $change_music("Matrix Credits")
    scene black with diss
    call show_credits