import time
import datetime
from itertools import repeat
import sys
import os


name = str(input("Hey whats your name?"))
print("Hi",name, "You are a falsely convicted prisoner ⛓️⛓️⛓️ and today's mission is to escape prison 💥")
time.sleep(1)
print("I am your cell mate, I'll help you and im coming with you. We have built a tunnel 🕳️ in the back of our cell which is hidden underneath a tile"
"this is our way out, but we need the right timing and distraction to successfully escape")
time.sleep(1)
print("you are going to make these decisions, choose wisely")
time.sleep(1)
print("right now it's 4 in the morning, before we start, we have to decide at what time of the day we want to escape")


while True:
    try:
        escape_time = int(input("Should we escape \n1. in the morning,\n 2. in the afternoon or\n 3. at night?\n "
                                "Type in the number of your choice: "))
        if escape_time in [1, 2, 3]:
            break
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Please enter a valid number.")

if escape_time == 1:
    while True:
        try:
            distraction_morning = int(input("Okay, let's distract the guard\n"
                                            " 1.Throw a toothbrush out on the hallway to distract him\n"
                                            " 2.make loud screaming noises\n"
                                            " 3.Stay quiet\n"
                                            " type in the number of your choice:"))
            if distraction_morning in [1, 2, 3]:
                break
            else:
                print("Please choose a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

    if distraction_morning == 1:
        print("alright, I'll throw it now...")
        time.sleep(1)
        print("okay the guard is distracted now, let's get to the tunnel 🕳️ and escape!!!")


    if distraction_morning ==2:
        print("AHHHHHHHHHH")
        time.sleep(1)
        print("oh no, that was a bad idea the guard is coming towards our cell...")
        time.sleep(0.5)
        print("Guard 👮:'What the hell is going on here??? You guys are waking up the entire cell block."
                  "You're going to be in solitary confinment fot at least one week!'")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("GAME OVER")
        exit()

    if distraction_morning == 3:
            print("Alright, let's stay quiet, help me to lift up the tile in the back of our cell to access the tunnel 🕳️")

    if distraction_morning == 1 and distraction_morning == 3:
        print("Okay, we made it, we're in the tunnel 🕳️ now, let´s crawl towards the end and then we should be in freedom.")


if escape_time == 2:
    time.sleep(0.5)
    print("5 o'clock")
    time.sleep(0.5)
    print("6 o'clock")
    time.sleep(0.5)
    print("7 o'clock")
    time.sleep(0.5)
    print("8 o'clock")
    time.sleep(0.5)
    print("9 o'clock")
    time.sleep(0.5)
    print("10 o'clock")
    time.sleep(0.5)
    print("11 o'clock")
    time.sleep(0.5)
    print("12 o'clock")
    time.sleep(0.5)
    print("RINGGGGGG it's lunchtime, let's go grab some food")
    time.sleep(0.5)
    print("the burger was delicious, now everyone is talking and walking around with their lunch trays, let's use the bustle for our escape")

    while True:
        try:
            lunch_escape = int(input("Should we:\n"
                                     "1. Run out of the cafeteria straight to our cell to use the tunnel🕳️?\n"
                                     "2. Sneak out carefully?\n"
                                     "3. Throw a burger in the face of one of the guards to distract them?\n"
                                     "Type the number of your choice: "))

            if lunch_escape == 1:
                print("Okay, run", name, "let's get out of here!")
                time.sleep(1)
                print(
                    "Okay, we're back in our cell. Now lift up the tile in the back real quick so we can get into the tunnel🕳️.")
                break

            elif lunch_escape == 2:
                print("Pssst... be as quiet and sneaky as possible. It's going to take some time but if we "
                      "stay quiet we'll be in freedom soon.")
                time.sleep(4)
                print("Finally back at our cell. Now let's make our way through the tunnel🕳️.")
                break

            elif lunch_escape == 3:
                print("BOOM! Here you go, guard! Do you like that burger?")
                time.sleep(1)
                print("Haha, he ate sh*t.")
                time.sleep(1)
                print(
                    "Other guard: 'HEY! GET ON THE GROUND RIGHT NOW AND SHOW ME YOUR HANDS! YOU GUYS CAN'T START A PRISON RIOT!'")
                time.sleep(1)
                print("...")
                print("GAME OVER")
                exit()
            else:
                print("Please enter a number between 1 and 3.")

        except ValueError:
            print("Enter a valid number.")

if escape_time == 3:
    time.sleep(0.25)
    print("5 o'clock")
    time.sleep(0.25)
    print("6 o'clock")
    time.sleep(0.25)
    print("7 o'clock")
    time.sleep(0.25)
    print("8 o'clock")
    time.sleep(0.25)
    print("9 o'clock")
    time.sleep(0.25)
    print("10 o'clock")
    time.sleep(0.25)
    print("11 o'clock")
    time.sleep(0.25)
    print("12 o'clock")
    time.sleep(0.25)
    print("1 o'clock")
    time.sleep(0.25)
    print("2 o'clock")
    time.sleep(0.25)
    print("3 o'clock")
    time.sleep(0.25)
    print("4 o'clock")
    time.sleep(0.25)
    print("5 o'clock")
    time.sleep(0.25)
    print("6 o'clock")
    time.sleep(0.25)
    print("7 o'clock")
    time.sleep(0.25)
    print("8 o'clock")
    time.sleep(0.25)
    print("Alright, it's 9 pm now, everyone is going back to their cells from dinner, this is our chance")

    while True:
        try:
            distraction_night = int(input("should we:\n"
                "1. leave right now because there is a bustle going on with everyone going back to their cells \n"
              "2. Wait until our inmates go for a shower\n"
              "3. start a big fight to alarm the guards and use the chaos to escape?"))
            if distraction_night == 1:
                print("Okay, pssst let's get back in our cell")
                time.sleep(1)
                print("now quietly lift up the tile and....")
                time.sleep(0.25)
                print("...we're in the tunnel🕳️")
                break

            if distraction_night == 2:
                print("Okay, so we wait...")
                time.sleep(2.5)
                print("Now everyone is in the shower and the guards are busy, lift up the tile real quick and... we're in the tunnel🕳️")
                break

            if distraction_night == 3:
                print("Okay I'll try to trashtalk one of the big guys")
                time.sleep(0.5)
                print("'Hey dumbass, why you walkin around tryna look tough, watch out or i'ma whoop your ass buddy!'")
                time.sleep(1)
                print("fellow inmate:'HUH? WHAT YOU SAY? IM'A BEAT YOUR ASS MAN...")
                time.sleep(0.25)
                print("IN FACT IM GONNA KNOCK OUT BOTH OF YOU!!!")
                time.sleep(0.5)
                print("💥BOOOOM... you gut knocked out...💥")
                time.sleep(0.25)
                print("GAME OVER")
                break
                exit()
            else:
                print("Please type a number between 1 and 3.")
        except ValueError:
            print("Enter a valid number.")

while True:
    time.sleep(1)
    print(
        "Oh no, look the tunnel🕳️ has collapsed right here... but I have a spoon, we could use it to dig through the collapsed part")
    try:
        use_spoon = int(input("1. Use the spoon to make our way through the tunnel🕳️\n2. Go back to the cell\nType your choice: "))
        if use_spoon ==1:
            print("Okay, this is going to take some time...")
            time.sleep(3)
            print("But here we go, the way is open now. Let's go!")
            time.sleep(1)
            print(f"Finally we're free!!! Thanks for the help, {name}. We're a great team!")
            exit()
            break
        elif use_spoon ==2:
            print("Okay, then let's go back.")
            time.sleep(1)
            print("Oh sh*t, the guards found out. They are at the cell. I think they found our...")
            print("Guard 👮: 'HEY, WHAT ARE YOU GUYS DOING THERE?! YOUR SENTENCE IS GOING TO BE EXTENDED FOR AT LEAST A YEAR!!!'")
            print("...GAME OVER")
            exit()
            break
        else:
            print("Type 1 or 2 please.")
    except ValueError:
        print("Enter a valid number.")

