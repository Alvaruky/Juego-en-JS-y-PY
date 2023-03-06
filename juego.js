input.onButtonPressed(Button.A, function () {
    LedAbajo.move(-1)
})
function Objeto1() {
    Objeto = game.createSprite(randint(0, 4), 0)
    for (let index = 0; index < 4; index++) {
        basic.pause(500)
        Objeto.change(LedSpriteProperty.Y, 1)
    }
}
input.onButtonPressed(Button.B, function () {
    LedAbajo.move(1)
})
let Objeto: game.LedSprite = null
let LedAbajo: game.LedSprite = null
LedAbajo = game.createSprite(2, 4)
Objeto1()
basic.forever(function () {
    if (Objeto.isTouching(LedAbajo)) {
        basic.showIcon(IconNames.Yes)
        Objeto.delete()
        Objeto1()
    } else {
        basic.showIcon(IconNames.No)
        game.gameOver()
    }
})

