## USO DE ALGORITMOS VORACES
import tkinter as tk
from tkinter import ttk, messagebox



clientes = [
    {"nombre": "Cliente: LENIN","horario": "08:00"},
    {"nombre": "Cliente: YULI","horario": "09:00"},
    {"nombre": "Cliente: DAVID","horario": "10:00"},
    {"nombre": "Cliente: PATRICK","horario": "11:00"},
    {"nombre": "Cliente: MARQUINO","horario": "12:00"},
]

vehiculos = [
    "Camion 1",
    "Camion 2",
    "Furgoneta"
]

centro = "Centro de Distribucion Logistica"


distancias = [
    [0, 8, 12, 15, 20, 10],
    [8, 0, 5, 7, 18, 11],
    [12, 5, 0, 9, 10, 6],
    [15, 7, 9, 0, 8, 9],
    [20, 18, 10, 8, 0, 7],
    [10, 11, 6, 9, 7, 0]
]



def ruta_voraz():

    n = len(clientes)
    visitados = [False] * n

    ruta = []
    actual = 0
    distancia_total = 0

    for _ in range(n):

        menor = float("inf")
        siguiente = -1

        for i in range(n):
            if not visitados[i]:

                distancia = distancias[actual][i+1]

                if distancia < menor:
                    menor = distancia
                    siguiente = i

        visitados[siguiente] = True
        ruta.append(siguiente)
        distancia_total += menor

        actual = siguiente + 1

    distancia_total += distancias[actual][0]

    return ruta, distancia_total

## USO DEL BACKTRACKING
def ruta_backtracking():
    n = len(clientes)
    ciudades = list(range(n))
    mejor_ruta = []
    distancia_minima = float('inf')
    for p in itertools.permutations(ciudades):
        ruta_actual = [0] + [i+1 for i in p] + [0]
        distancia_actual = 0
        for i in range(len(ruta_actual) - 1):
            distancia_actual += distancias[ruta_actual[i]][ruta_actual[i+1]]
        if distancia_actual < distancia_minima:
            distancia_minima = distancia_actual
            mejor_ruta = list(p)
    return mejor_ruta, distancia_minima



def calcular():

    ruta, total = ruta_voraz()

    salida.delete(1.0, tk.END)

    salida.insert(tk.END, "CENTRO DE DISTRIBUCION LOGISTICA\n")
    salida.insert(tk.END, centro + "\n\n")

    salida.insert(tk.END, "VEHÍCULO DISPONIBLES\n")
    salida.insert(tk.END, comboVehiculo.get() + "\n\n")

    salida.insert(tk.END, "RUTA OPTIMA \n\n")
    salida.insert(tk.END, "CLIENTES QUE RECIBIRAN SUS PEDIDOS \n\n")

    paso = 1

    for i in ruta:
        salida.insert(
            tk.END,
            f"{paso}. {clientes[i]['nombre']}   -  Horario: {clientes[i]['horario']}\n"
        )
        paso += 1

    salida.insert(tk.END, "\n")
    salida.insert(tk.END, f"Distancia Total: {total} km")



ventana = tk.Tk()
ventana.title("Optimizacion de rutas de entrega en una empresa de logistica_Grupo06")
ventana.geometry("700x600")
ventana.configure(bg="#E8F0FE")

titulo = tk.Label(
    ventana,
    text="OPTIMIZACION DE RUTAS DE ENTREGA",
    font=("Arial",16,"bold"),
    bg="#E8F0FE"
)

titulo.pack(pady=10)

frame = tk.Frame(ventana,bg="#E8F0FE")
frame.pack()

tk.Label(frame,text="Centro de Distribución:",bg="#E8F0FE",
font=("Arial",11,"bold")).grid(row=0,column=0,sticky="w")

tk.Label(frame,text=centro,bg="#E8F0FE").grid(row=0,column=1)

tk.Label(frame,text="Vehículo:",bg="#E8F0FE",
font=("Arial",11,"bold")).grid(row=1,column=0,sticky="w")

comboVehiculo = ttk.Combobox(frame,values=vehiculos,width=20)
comboVehiculo.current(0)
comboVehiculo.grid(row=1,column=1,pady=5)

tk.Label(frame,text="Clientes:",bg="#E8F0FE",
font=("Arial",11,"bold")).grid(row=2,column=0,sticky="nw")

textoClientes = ""

for c in clientes:
    textoClientes += f"{c['nombre']}  ({c['horario']})\n"

tk.Label(frame,text=textoClientes,bg="#E8F0FE",justify="left").grid(row=2,column=1)

boton = tk.Button(
    ventana,
    text="Calcular Ruta",
    command=calcular,
    bg="green",
    fg="white",
    font=("Arial",12,"bold")
)

boton.pack(pady=15)

salida = tk.Text(ventana,width=70,height=20)
salida.pack()

ventana.mainloop()
