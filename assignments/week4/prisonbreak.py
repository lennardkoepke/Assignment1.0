#constants
import time

short_pause=0.5
long_pause=1.0
PLAYER_NAME=""
GAME_OVER="GAME OVER!"
ESCAPE_TIME_OPTIONS= ["morning","afternoon","night"]
ESCAPE_MORNING_OPTIONS= ["Throw a toothbrush in the hallway","Scream loudly","Stay quiet"]
ESCAPE_AFTERNOON_OPTIONS= ["Run to the cell", "Sneak out", "Throw a burger at a guard"]
ESCAPE_NIGHT_OPTIONS= ["Leave now","Wait for shower time", "Start a fight"]
TUNNEL_SCENE_OPTIONS= ["Use spoon to dig"," Go back to cell"]
#adding pause functions
def pause(seconds=short_pause):
    time.sleep(seconds)
#game over function
def print_game_over():
    print(GAME_OVER)
    exit()

#scenes

def intro():
    global PLAYER_NAME
    PLAYER_NAME= input("Hey, what's your name? ")
    print(f"{PLAYER_NAME},you are a falsely convicted prisoner ⛓️⛓️⛓️ and today's mission is to escape prison 💥")
    pause(long_pause)
    print(
        f"I am your cellmate. I'll help you. We have built a tunnel 🕳️ hidden underneath a tile in the back of our cell.")
    pause()
    print("You are going to make these decisions. Choose wisely.")
    pause()
    print("Right now it's 4 in the morning. We need to decide when to escape.")


def choose_escape_time():
    while True:
        try:
            choice = int(input(f"Should we escape \n1. in the {ESCAPE_TIME_OPTIONS[0]},\n 2. in the {ESCAPE_TIME_OPTIONS[1]} or\n 3. at {ESCAPE_TIME_OPTIONS[2]}?\n "
                                    "Type in the number of your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")


def escape_morning():
    while True:
        try:
            choice = int(input(f"Distract the guard:\n1. {ESCAPE_MORNING_OPTIONS[0]}\n2. {ESCAPE_MORNING_OPTIONS[1]}\n3. {ESCAPE_MORNING_OPTIONS[2]}\nChoice: "))
            if choice == 1:
                print("Alright, I'll throw it now...")
                pause()
                print(f"The guard is distracted. Let's get to the tunnel 🕳️ and escape!")
                return True
            elif choice == 2:
                print("AHHHHHH!")
                pause()
                print("Bad idea! The guard is coming...")
                pause()
                print("Guard 👮: 'You're going to solitary for a week!'")
                print_game_over()
            elif choice == 3:
                print(f"Stay quiet and help lift the tile to the tunnel 🕳️")
                return True
            else:
                print("Choose 1, 2 or 3.")
        except ValueError:
            print("Enter a valid number.")



def escape_afternoon():
    for hour in range(5, 13):
        pause(0.25)
        print(f"{hour} o'clock")
    print("RINGGG! It's lunchtime. Let's use the bustle to escape.")

    while True:
        try:
            choice1 = int(input(f"Choose how to escape:\n1. {ESCAPE_AFTERNOON_OPTIONS[0]}\n2. {ESCAPE_AFTERNOON_OPTIONS[1]}\n3. {ESCAPE_AFTERNOON_OPTIONS[2]}\nChoice: "))
            if choice1 == 1:
                print(f"Run, {PLAYER_NAME}! Back to the cell!")
                pause()
                print(f"Lift the tile... into the tunnel 🕳 we go!")
                return True
            elif choice1 == 2:
                print("Be sneaky... this will take time.")
                pause(4)
                print(f"Made it! Back at the cell. Enter the tunnel 🕳.")
                return True
            elif choice1 == 3:
                print("BOOM! Burger to the face!")
                pause()
                print("Other guard: 'GET ON THE GROUND!'")
                print_game_over()
            else:
                print("Choose 1, 2 or 3.")
        except ValueError:
            print("Enter a valid number.")



def escape_night():
    for hour in range(5, 21):
        pause(0.25)
        print(f"{hour} o'clock")
    print("It's 9 PM. Everyone's returning from dinner. This is our chance.")

    while True:
        try:
            choice2 = int(input(f"Choose how to escape:\n1. {ESCAPE_NIGHT_OPTIONS[0]}\n2. {ESCAPE_NIGHT_OPTIONS[1]}\n3. {ESCAPE_NIGHT_OPTIONS[2]}\nChoice: "))
            if choice2 == 1:
                print("Quick! Back to the cell.")
                pause()
                print(f"Lift the tile... into the tunnel 🕳")
                return True
            elif choice2 == 2:
                print("We wait...")
                pause(2.5)
                print(f"Everyone's in the shower. Into the tunnel 🕳 now!")
                return True
            elif choice2 == 3:
                print("hey buddy, you walkin around tryna look tough, ima beat your a**")
                print("WHAT THE F*CK ARE YOU SAYING; IMA KNOCK YOU OUT!")
                pause()
                print("BOOM! You got knocked out.")
                print_game_over()
            else:
                print("Choose 1, 2 or 3.")
        except ValueError:
            print("Enter a valid number.")



def tunnel_scene():
    print(f"Oh no! The tunnel 🕳️ has collapsed.")
    pause()
    choice3 = int(input(f"1. {TUNNEL_SCENE_OPTIONS[0]}\n2. {TUNNEL_SCENE_OPTIONS[1]}\nChoice: "))
    if choice3 == 1:
        print("Start digging...")
        pause(3)
        print("Tunnel cleared. Let's go!")
        pause()
        print(f"Finally free! Thanks for the help, {PLAYER_NAME}. We're a great team!")
    elif choice3 == 2:
        print("Heading back...")
        pause()
        print("Guard: 'WHAT ARE YOU DOING?! A YEAR MORE ADDED!'")
        print_game_over()
    else:
        print("Invalid choice. Game ends.")
        print_game_over()


def main():
    intro()
    time_choice = choose_escape_time()
    if time_choice == 1:
        success = escape_morning()
    elif time_choice == 2:
        success = escape_afternoon()
    elif time_choice == 3:
        success = escape_night()
    else:
        print_game_over()
        return

    if success:
        tunnel_scene()


if __name__ == "__main__":
    main()