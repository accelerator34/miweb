import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

#interfaz
def crearwidghets():
    etiquetaGuardar = Label(vn, text = "Guardar como: ", font = ("", 10, "bold"))
    etiquetaGuardar.grid(row=1, column = 0, pady= 5, padx=5)

    vn.textoGuardar = Entry(vn, width = 30)
    vn.textoGuardar.grid(row=1, column=1, padx=5, pady=5)

    botonGuardar = Button(vn, text= "Navegar", width= 10, command= navegar)
    botonGuardar.grid(row=1, column=2, pady=5, padx=5)

    botonCaptura = Button(vn, text= "Captura", padx=5, pady=5, command= captura)
    botonCaptura.grid(row=2, column=1, padx=5, pady=5)

#Funcion navegar y guardar
def navegar():
    vn.archivoNombre = filedialog.asksaveasfilename(title="Guardar como", initialdir = "C:\\Users\\PERSONAL\\Desktop",defaultextension=".png",filetypes= (("Archivo Png", "*.png"), ("Todos Archivos", "*.*")))


    vn.textoGuardar.insert("1", vn.archivoNombre)

def captura():
    captura = pyautogui.screenshot()

    captura.save(vn.archivoNombre)
    messagebox.showinfo("Exito", "Captura Guardada")


vn = tk.Tk()
#vn.geometry("400x400")
vn.title("Captura de pantalla")
crearwidghets()
vn.mainloop()