function Timetimer () {
    Y = 0
    X = 0
    while (Y < 5) {
        if (X <= 4) {
            basic.pause(200)
            led.unplot(X, Y)
            X += 1
            if (X == 2 && Y == 2) {
                music.setVolume(125)
                music.playTone(262, music.beat(BeatFraction.Whole))
            }
        } else if (X > 4) {
            X = 0
            Y += 1
        }
    }
}
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    Timetimer()
})
input.onButtonPressed(Button.B, function () {
	
})
let X = 0
let Y = 0
soundExpression.hello.play()
