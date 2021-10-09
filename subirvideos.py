import pyautogui as pg ,webbrowser as web ,time as tm
name=input("Como se va llamar : ")#Le pregunta al usuario el nombre del video
n=name.lower()#convierte el nombre a minisculas 
ir = n.find('quimica')!=-1 or n.find('fisica')!=-1 or n.find('logica')!=-1 #valida si es de irwing  
web.open('https://studio.youtube.com/channel/UCxXE5uqxeC-9wBdTteT1VnA/videos?d=ud')#Abre el navegador en youtube estudio
currentMouseX, currentMouseY = pg.position()#mira la posicion del moouse 
tm.sleep(15)
#Apreta el boton de subir videos 
pg.click(708,527) #elige el video
#imprime las coordenadas del mouse
print({
    "x":currentMouseX,
    "y":currentMouseY
})
tm.sleep(4)
pg.click(456,191) #elige el video a subir 
pg.press("enter")
tm.sleep(5)
pg.write(name)#escribe el nombre del video
if ir:
    pg.click(1088,558)#si es de irwing copia el link
tm.sleep(2)
pg.click(1119,650)#Apreta el boton den siguiente para que baje
tm.sleep(2)
pg.click(256,591) #No es de ninos 
for i in range (3):
 pg.click(1119,650)#Siguiente 
# si es de irwing le da oculto caso contrario publico   
tm.sleep(2)
if ir:
    pg.press("down")
    print(0)
else:
    pg.press('up')
tm.sleep(3)
pg.click(1119,650) # le da a subir
#si es de irwing abre la pagina para meter el formulario de videos
if ir:
    web.open("http://192.168.0.8") #Abre pagina de videos 
    tm.sleep(5)
    pg.click(627,121) #Click en el nombre
    tm.sleep(1)
    pg.write(name)  #Escribe el nombre 
    pg.click(667,141)#Click en el link
    pg.click(667,141)
    tm.sleep(2)
    pg.hotkey('ctrl','v')
    pg.click(636,158)#Click al boton de mandar info
pg.click(708,741)#abre el explorador de archivos
tm.sleep(4)
pg.click(72,261)#Videos 
pg.click(456,169)#Click al primer video
pg.hotkey ('ctrl', 'x')#Corta el video
pg.click(347,161)
pg.click(347,161)#Se mete a la carperta de Subir videos 
tm.sleep(2)
pg.hotkey ('ctrl', 'v')#Pega el video
