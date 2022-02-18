import keyboard as kb
import time
import pyautogui as pg

# taken: (56, 167, 231)
# not taken: (255, 255, 255)
# search fullscreen: x=858, y=88
# result fullscreen: x = 1111, y = 292
# ok fullscreen: x=1750, y=978

# array to store all words that are not available and unavailable
available = []
availIndex = []
notAvail = []


# can change coordinates whenever
def doAction(name, resultX, resultY):
    # pg.click(searchX, searchY)
    time.sleep(0.1)
    # delete the written words
    kb.send('ctrl+a, delete')
    time.sleep(0.1)
    # write new word
    # for some reason .write enters? so i added an extra.
    kb.write(name, delay=0.05)
    time.sleep(0.05)
    kb.send('enter')
    time.sleep(0.1)
    kb.send('enter')
    time.sleep(0.1)
    rgb = pg.pixel(resultX, resultY)
    time.sleep(0.1)
    kb.send('enter')
    print("RGB: " + str(rgb))
    return rgb
    
    


count = 1

with open('names.txt', 'r') as n:
    print("first click")
    pg.click(858, 88)
    time.sleep(0.5)
    for name in n:
        rgb = doAction(name, 1111, 292)
        # we compare by rgb. assume that we can just make use of the color values to determine
        if (rgb == (56, 167, 231)):
            print(name.strip() + " is not available!\n")
            notAvail.append(name)
        else:
            print(name.strip() + " is available!\n")
            available.append(name)
            availIndex.append(count)
        count+= 1



availFile = open("available.txt", 'w')
for names in available:
    availFile.write(names)


print("Index: " + availIndex)
print("count: " + count)






