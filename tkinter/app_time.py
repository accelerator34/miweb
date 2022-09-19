#py -m pip install requests
#user_random, delavidaconsejero@gmail.com, therandom324
#9aec2f752278e431d86e240ee64156c6
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
#19.54878, -71.70829


from tkinter import *
import requests

def clima(ciudad):
    API_Key = "9aec2f752278e431d86e240ee64156c6"
    URL = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"
    parametros = {"APPID": API_Key, "q": ciudad, "units": "metric"}
    response = requests.get(URL, params = parametros)
    print(response.json())

app_ventana = Tk()
app_ventana.geometry("340x540")

texto_ciudad = Entry(app_ventana, font=("Courier", 20, "normal"), justify= "center")
texto_ciudad.pack(padx= 30, pady=40)

boton_clima = Button(app_ventana, text= "Obtener Clima", font=("Courier", 20, "normal"), command = lambda: clima(texto_ciudad.get()))
boton_clima.pack()

mostrar_clima = Label(text= "weather", font= ("Courier", 20, "normal"))
mostrar_clima.pack()

app_ventana.mainloop()

#Me cago en el puto error de mierda que nose ni cual es