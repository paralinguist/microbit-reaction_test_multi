from microbit import *
import random
import radio

searching = True
listening = True
sender = False
display.show(Image.TARGET)
wait_time = random.randint(2000, 10000)
radio.on()
while searching:
    if button_b.was_pressed():
        radio.send(str(wait_time))
        display.show("S")
        sender = True
        while listening:
            confirmation = radio.receive()
            if confirmation is not None and int(confirmation) == wait_time:
                listening = False
                searching = False
                display.show(Image.YES)
            else:
                sleep(10)
    elif button_a.was_pressed():
        #Need to do this to reset the number of times A was pressed.
        button_a.get_presses()
        display.show("R")
        while listening:
            wait_time = radio.receive()
            if wait_time is not None:
                radio.send(wait_time)
                wait_time = int(wait_time)
                listening = False
                searching = False
                display.show(Image.YES)
            else:
                sleep(10)
    else:
        sleep(50)

radio.off()
listening = True
display.show(Image.ASLEEP)
sleep(wait_time)
if button_a.get_presses():
    display.show(Image.NO)
else:
    display.show(Image.FABULOUS)
    waiting = True
    reaction_time = 0
    while waiting:
        if button_a.is_pressed():
            waiting = False
        sleep(10)
        reaction_time = reaction_time + 10
    display.show(Image.YES)
    sleep(1000)
    radio.on()
    while listening:
        if sender and listening:
            radio.send(str(reaction_time))
            display.show(Image.CLOCK1)
            sleep(10)
            opponent_time = radio.receive()
            if opponent_time is not None:
                listening = False
        elif not sender:
            opponent_time = radio.receive()
            if opponent_time is not None:
                radio.send(str(reaction_time))
                listening = False
            sleep(10)
    opponent_time = int(opponent_time)
    if opponent_time > reaction_time:
        display.show(Image.HAPPY)
    elif opponent_time < reaction_time:
        display.show(Image.SAD)
    else:
        display.show(Image.DUCK)