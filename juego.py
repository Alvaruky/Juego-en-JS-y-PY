def on_button_pressed_a():
    LedAbajo.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def Objeto1():
    global Objeto
    Objeto = game.create_sprite(randint(0, 4), 0)
    for index in range(4):
        basic.pause(500)
        Objeto.change(LedSpriteProperty.Y, 1)

def on_button_pressed_b():
    LedAbajo.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Objeto: game.LedSprite = None
LedAbajo: game.LedSprite = None
LedAbajo = game.create_sprite(2, 4)
Objeto1()

def on_forever():
    if Objeto.is_touching(LedAbajo):
        basic.show_icon(IconNames.YES)
        Objeto.delete()
        Objeto1()
    else:
        basic.show_icon(IconNames.NO)
        game.game_over()
basic.forever(on_forever)