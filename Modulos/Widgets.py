import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

fecha_seleccionada = None  # Variable global para almacenar la fecha seleccionada

def obtener_fecha(root, cal):
    global fecha_seleccionada
    fecha_seleccionada = cal.get_date()
    root.destroy()  # Cierra la ventana después de obtener la fecha

def getdatecalendar(iniciolimite, finlimite):
    global fecha_seleccionada
    # Convertir las fechas de string a objetos datetime
    iniciolimite_dt = datetime.strptime(iniciolimite, "%Y-%m-%d")
    finlimite_dt = datetime.strptime(finlimite, "%Y-%m-%d")

    root = tk.Tk()
    root.title("Seleccionar Fecha")

    cal = Calendar(root, selectmode="day", year=iniciolimite_dt.year, month=iniciolimite_dt.month, day=iniciolimite_dt.day, mindate=iniciolimite_dt, maxdate=finlimite_dt)
    cal.pack(padx=10, pady=10)

    btn_obtener_fecha = ttk.Button(root, text="Obtener Fecha", command=lambda: obtener_fecha(root, cal))
    btn_obtener_fecha.pack(pady=10)

    root.mainloop()
    
    return fecha_seleccionada


# Llamada a la función y luego impresión de la fecha seleccionada


