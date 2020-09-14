from microbit import *

while True:
    display.show(Image.RABBIT)
    sleep(2000)
    display.show(Image(
        "99000:"
        "00990:"
        "00099:"
        "00990:"
        "99000"))
    sleep(2000)
    display.show(Image.SNAKE)
    sleep(2000)
    display.show(Image.SKULL)
    sleep(2000)