import pyautogui as pg ,webbrowser as web
def cli(x,y):
    for i in range(2):
        pg.click(x,y)
cli(1098,273)
cli(1217,397)
cli(1207,255)
web.open("https://ajsajismossw.000webhostapp.com/")
print("Ejecutado con exito")