import pyautogui as pg,time as tm
import random as r
pg.FAILSAFE = True
# tm.sleep(7)
# currentMouseX, currentMouseY = pg.position()#mira la posicion del moouse 
# #imprime las coordenadas del mouse
# print({
#     "x":currentMouseX,
#     "y":currentMouseY
# })
c=0
while True:
    for q in range(5):
        tm.sleep(60)
        for i in range(3):
            d2=r.randint(5,15)
            tm.sleep(d2)
            pg.click(725,670)
            pg.write('@lunay')
            pg.click(1123,671)
            c=c+1
            print("Se a comentado "+str(c)+" veces")
    d1=r.randint(3,10)
    pg.sleep(d1*60)

        
    