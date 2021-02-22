# script to press and hold based on what pickaxes you have in your hotbar
from pynput.mouse import Button, Controller
from pynput import keyboard
import math
import time as t
#lists are organized (wood, stone, iron, diamond, netherite, golden)
#stoneTime = [1.5, 0.75, 0.5, 0.4, 0.35, 0.25]
toolMultiplier = [2, 4, 6, 8, 9, 12]
durability = [59, 131, 250, 1561, 2031, 32]
hardness = 2
mouse = Controller()

def calcSeconds(multiplier, efficiency):
    speedMultiplier = multiplier
    if(efficiency > 0):
        speedMultiplier += efficiency**2 + 1
    damage = float(speedMultiplier) / float(hardness) / float(30)
    if(damage > 1):
        return 1/20
    ticks = math.ceil(1/damage)
    seconds = ticks/20
    return seconds

def startMining(hotbar, toolMultiplier, eff, durability):
    times = []
    for i in range(0, len(hotbar)):
        timePerBlock = calcSeconds(toolMultiplier[i], eff[i])
        times.append(timePerBlock*durability[i])

    for length in times:
        passed = 0
        mouse.press(Button.left)
        while(passed < length):
            #hold left click
            t.sleep(1)
            passed += 1
        mouse.scroll(0, 1)
        print("pickaxe is done")
        #scroll down by 1 tick
    mouse.release(Button.left)

def on_press(key):
    print("keypress read")
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def wait_for_user_input(hotbar, toolMultiplier, eff, durability):
    #listener = Listener(on_press=onPress, on_release=onRelease)
    #listener.start()
    #listener.join()
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        print("listening for keypress")
        listener.join()
        print("join complete")
    print("Starting to mine")
    # startMining(hotbar, toolMultiplier, eff, durability)



pick = ""
print("Please enter the type of pickaxe(s)")
hotbar = []
efficiency = []
# while(True):
#     pick = input("enter b to stop entering picks\n")
#     pick = pick.lower()
#     if(len(hotbar) > 10):
#         break
#     elif(pick == "b"):
#         break
#     elif(pick == "wood"):
#         eff = int(input("Please enter the level of efficiency (if none, enter 0)\n"))
#         efficiency.append(eff)
#         hotbar.append(toolMultiplier[0])
#         print("wood added")
#     elif(pick == "stone"):
#         eff = int(input("Please enter the level of efficiency (if none, enter 0)\n"))
#         efficiency.append(eff)
#         hotbar.append(toolMultiplier[1])
#         print("stone added")
#     elif(pick == "iron"):
#         eff = int(input("Please enter the level of efficiency (if none, enter 0)\n"))
#         efficiency.append(eff)
#         hotbar.append(toolMultiplier[2])
#         print("iron added")
#     elif(pick == "diamond"):
#         eff = int(input("Please enter the level of efficiency (if none, enter 0)\n"))
#         efficiency.append(eff)
#         hotbar.append(toolMultiplier[3])
#         print("diamond added")
#     elif(pick == "netherite"):
#         eff = int(input("Please enter the level of efficiency (if none, enter 0)\n"))
#         efficiency.append(eff)
#         hotbar.append(toolMultiplier[4])
#         print("netherite added")
#     elif(pick == "gold"):
#         eff = int(input("Please enter the level of efficiency (if none, enter 0)\n"))
#         efficiency.append(eff)
#         hotbar.append(toolMultiplier[5])
#         print("gold added")
#     else:
#         print("invalid input")

# if(len(hotbar) == 0):
#     print("You will need to re-run this program and select a pick")

print("Press / on any software to start mining")
wait_for_user_input(hotbar, toolMultiplier, efficiency, durability)
#calculate how long to click for each pick, and iterate to the next pick





#Read pointer position
print('The current pointer position is {0}'.format(mouse.position))

