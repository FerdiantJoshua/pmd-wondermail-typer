import time
import keyboard

import pydirectinput

key_coord = {
    "ovr": (0,2),
    "del": (0,1),
    "end": (0,0),

    "N": (1,2),
    "+": (1,0),

    "1": (2,1),
    "-": (2,0),
    
    "C": (3,3),
    "P": (3,2),
    "2": (3,1),
    
    "Q": (4,2),
    "3": (4,1),
    
    "R": (5,2),
    "4": (5,1),
    "!": (5,0),

    "F": (6,3),
    "S": (6,2),
    "5": (6,1),
    "?": (6,0),
    
    "T": (7,2),
    "6": (7,1),
    
    "H": (8,3),
    "7": (8,1),
    
    "8": (9,1),
    
    "J": (10,3),
    "W": (10,2),
    "9": (10,1),
    
    "K": (11,3),
    "X": (11,2),
    "0": (11,1),
    "#": (11,0),
    
    "Y": (12,2),
    "%": (12,0),
    
    "M": (13,3),
    ".": (13,1)
}

if __name__ == "__main__":
    pydirectinput.PAUSE = 0.04
    while(True):
        curr_coordinate = [1,2]
        print("Type the wonder code, or enter 'e' to exit...")
        inp = input()
        if (inp == "e"): break
        wondercode = inp.replace(" ", "")
        print("press right Esc to start typing")
        keyboard.wait("esc")
        for c in wondercode:
            target = key_coord[c]
            print(f"target: {c} in {target}, curr_coordinate: {curr_coordinate}")

            
            if target[0] > curr_coordinate[0]:
                distance = target[0]-curr_coordinate[0]
                pydirectinput.press("right", presses=distance, interval=0, _pause=False)
                curr_coordinate[0] += distance
                print(f"right, new coord: {curr_coordinate}")
            else:
                distance = curr_coordinate[0]-target[0]
                pydirectinput.press("left", presses=distance, interval=0, _pause=False)
                curr_coordinate[0] -= distance
                print(f"left, new coord: {curr_coordinate}")
                

            if target[1] > curr_coordinate[1]:
                distance = target[1]-curr_coordinate[1]
                pydirectinput.press("up", presses=distance, interval=0, _pause=False)
                curr_coordinate[1] += distance
                print(f"up, new coord: {curr_coordinate}")
            else:
                distance = curr_coordinate[1]-target[1]
                pydirectinput.press("down", presses=distance,interval=0, _pause=False)
                curr_coordinate[1] -= distance
                print(f"down, new coord: {curr_coordinate}")

            # while target[0] != curr_coordinate[0]:
            #     if target[0] > curr_coordinate[0]:
            #         keyboard.press("right arrow")
            #         curr_coordinate[0] += 1
            #         print(f"right, new coord: {curr_coordinate}")
            #     else:
            #         keyboard.press("left arrow")
            #         curr_coordinate[0] -= 1
            #         print(f"left, new coord: {curr_coordinate}")
            #     time.sleep(0.1)
                    
            # while target[1] != curr_coordinate[1]:
            #     if target[1] > curr_coordinate[1]:
            #         keyboard.press("up arrow")
            #         curr_coordinate[1] += 1
            #         print(f"up, new coord: {curr_coordinate}")
            #     else:
            #         keyboard.press("down arrow")
            #         curr_coordinate[1] -= 1
            #         print(f"down, new coord: {curr_coordinate}")
            #     time.sleep(0.1)

            # keyboard.press("z")
            pydirectinput.press("z")
            print("char selected, continuing to next char..")
            print()

        print("Typing done!")
        print("Submitting the Wonder Code")
        pydirectinput.press("z", presses=3, interval=0.5, _pause=True)
        
        print("Waiting for game save...")
        time.sleep(4)
        print("Reentering Wonder Mail menu")
        pydirectinput.press("z", presses=4, interval=1, _pause=True)
        print()
