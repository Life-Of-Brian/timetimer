def Timetimer():
    global Y, X
    Y = 0
    X = 0
    while Y < 5:
        if X <= 4:
            basic.pause(200)
            led.unplot(X, Y)
            X += 1
            if X == 2 and Y == 2:
                music.set_volume(125)
                music.play_tone(262, music.beat(BeatFraction.WHOLE))
        elif X > 4:
            X = 0
            Y += 1

def on_button_pressed_a():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    Timetimer()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

X = 0
Y = 0
soundExpression.hello.play()