import keyboard as kb
import time
import pyautogui as pg


# this is for my own use. you can run coordinates.py to determine the coordinates respectively.

# ------------ first monitor!! --------------
# taken: (56, 167, 231)
# not taken: (255, 255, 255)
# search fullscreen: x=858, y=88
# result fullscreen: x = 1111, y = 292
# ok fullscreen: x=1750, y=978

# ----------- second monitor ---------------
# search fullscreen: x=2860, y=106
# result fullscreen: x=3037, y=294

# array to store all words that are not available
available = []
availIndex = []

# can change coordinates whenever
def doAction(name, resultX, resultY):
    # pg.click(searchX, searchY)
    time.sleep(0.15)
    # delete the written words
    kb.send('ctrl+a')
    time.sleep(0.2)
    kb.send('delete')
    time.sleep(0.15)
    # write new word
    # for some reason .write enters?
    kb.write(name, delay=0.05)
    time.sleep(0.15) 
    rgb = pg.pixel(resultX, resultY)
    time.sleep(0.15)
    kb.send('enter')
    print("RGB: " + str(rgb))
    return rgb
    
    


count = 1

start = time.time()
with open('filtered.txt', 'r') as n:
    print("first click")
    pg.click(2860, 106)
    time.sleep(0.5)
    for name in n:
        rgb = doAction(name, 3037, 294)
        # we compare by rgb. assume that we can just make use of the color values to determine
        if (rgb == (56, 167, 231)):
            print(str(count) + ": " + name.strip() + " is not available!\n")
        else:   
            print(str(count) + ": " + name.strip() + " is available!\n")
            available.append(name)
        count+= 1



availFile = open("available.txt", 'w')
for names in available:
    availFile.write(names)


print("count: " + str(count))
print("%s seconds taken" % (time.time() - start))





