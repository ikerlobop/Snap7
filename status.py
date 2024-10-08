import snap7
from snap7.util import *
from snap7.type import *
import tkinter as tk

client = snap7.client.Client()

actualizando = False  # Variable global para saber si se está actualizando


def conectar_plc(ip, rack, slot):
    try:
        client.connect(ip, int(rack), int(slot))
        if client.get_connected():
            print(f"Conectado al PLC en {ip} (Rack: {rack}, Slot: {slot})")
            obtener_estado_plc()  # Obtener estado inmediatamente después de conectar
            iniciar_actualizacion()  # Comenzar la actualización automática
            return True
        else:
            print(f"No se pudo conectar al PLC en {ip} (Rack: {rack}, Slot: {slot})")
            return False
    except Exception as e:
        print(f"Error al conectar: {e}")
        return False


def obtener_estado_plc():
    try:
        estado = client.get_cpu_state()
        if estado == 'S7CpuStatusRun':
            canvas.itemconfig(rectangulo, fill="green")
            label_status.config(text="RUN", bg="green")
        elif estado == 'S7CpuStatusStop':
            canvas.itemconfig(rectangulo, fill="orange")
            label_status.config(text="STOP", bg="orange")
        else:
            canvas.itemconfig(rectangulo, fill="gray")
            label_status.config(text="DESCONOCIDO", bg="gray")
    except Exception as e:
        print(f"Error al obtener el estado del PLC: {e}")
        canvas.itemconfig(rectangulo, fill="gray")
        label_status.config(text="ERROR", bg="gray")


def desconectar_plc():
    detener_actualizacion()  # Detener la actualización automática si está en progreso
    client.disconnect()
    print("Desconectado del PLC.")
    canvas.itemconfig(rectangulo, fill="gray")
    label_status.config(text="DESCONECTADO", bg="gray")


def actualizar_estado_cada_x_segundos(intervalo):
    global actualizando
    if actualizando:
        obtener_estado_plc()
        root.after(intervalo * 1000, lambda: actualizar_estado_cada_x_segundos(intervalo))  # Renovar después del intervalo


def iniciar_actualizacion():
    global actualizando
    if not actualizando:
        actualizando = True
        intervalo = int(entry_intervalo.get())  # Obtener el intervalo definido por el usuario
        actualizar_estado_cada_x_segundos(intervalo)
        print("Actualización automática iniciada.")


def detener_actualizacion():
    global actualizando
    if actualizando:
        actualizando = False
        print("Actualización automática detenida.")


root = tk.Tk()
root.title("Estado del PLC")

# Crear un canvas para el rectángulo
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack(pady=20)

# Dibujar un rectángulo en el canvas (inicialmente gris)
rectangulo = canvas.create_rectangle(50, 20, 150, 80, fill="gray")

label_status = tk.Label(root, text="DESCONECTADO", font=("Arial", 16), bg="gray", fg="white")
label_status.pack(pady=10)

label_ip = tk.Label(root, text="IP del PLC:")
label_ip.pack()

entry_ip = tk.Entry(root)
entry_ip.pack()

label_rack = tk.Label(root, text="Rack del PLC (por defecto 0):")
label_rack.pack()

entry_rack = tk.Entry(root)
entry_rack.insert(0, "0")  # Valor por defecto del rack
entry_rack.pack()

label_slot = tk.Label(root, text="Slot del PLC (por defecto 1):")
label_slot.pack()

entry_slot = tk.Entry(root)
entry_slot.insert(0, "1")
entry_slot.pack()

label_intervalo = tk.Label(root, text="Intervalo de actualización (segundos):")
label_intervalo.pack()

entry_intervalo = tk.Entry(root)
entry_intervalo.insert(0, "5")  # Intervalo por defecto de 5 segundos
entry_intervalo.pack()

btn_conectar = tk.Button(root, text="Conectar",
                         command=lambda: conectar_plc(entry_ip.get(), entry_rack.get(), entry_slot.get()))
btn_conectar.pack(pady=5)

btn_desconectar = tk.Button(root, text="Desconectar", command=desconectar_plc)
btn_desconectar.pack(pady=5)

root.mainloop()
