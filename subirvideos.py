import pyautogui as pg ,webbrowser as web ,time as tm
name=input("Como se va llamar : ")
n=name.lower()
ir = n.find('quimica')!=-1 or n.find('fisica')!=-1 or n.find('biologia')!=-1 
web.open('https://studio.youtube.com/channel/UCxXE5uqxeC-9wBdTteT1VnA/videos?d=ud')
currentMouseX, currentMouseY = pg.position()
tm.sleep(15)
#Apreta el boton 
pg.click(708,527)
print({
    "x":currentMouseX,
    "y":currentMouseY
})
tm.sleep(4)
pg.click(340,286)
pg.press("enter")
tm.sleep(5)
pg.write(name)
if ir:
    pg.click(1088,558)
tm.sleep(2)
pg.click(1119,650)
tm.sleep(2)
pg.click(274,563) 
pg.click(1119,650)
pg.click(1119,650)
pg.click(1119,650)
if ir:
    pg.press("down")
    print(0)
else:
    pg.press('up')
tm.sleep(3)
pg.click(1119,650)
if ir:
    web.open("http://192.168.0.8")
    tm.sleep(5)
    pg.click(627,121)
    tm.sleep(1)
    pg.write(name)
    pg.click(621,148)
    pg.hotkey('ctrl','v')
    pg.click(636,158)
pg.click(123,736)
tm.sleep(4)
pg.click(79,466)
pg.click(751,170)
pg.hotkey ('ctrl', 'x')
pg.click(653,153)
pg.click(653,153)
tm.sleep(2)
pg.hotkey ('ctrl', 'v')
