import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def validar_formulario():
    # Obtener los datos de los campos
    nombre = entry_nombre.get()
    email = entry_email.get()
    fecha_nac = entry_fecha.get()
    telefono = entry_telefono.get()
    
    # Validaciones básicas
    errores = []
    
    if not nombre:
        errores.append("El nombre es obligatorio")
    
    if "@" not in email or "." not in email:
        errores.append("Ingrese un correo electrónico válido")
    
    try:
        datetime.strptime(fecha_nac, "%d/%m/%Y")
    except ValueError:
        errores.append("La fecha debe estar en formato DD/MM/AAAA")
    
    if not telefono.isdigit() or len(telefono) < 8:
        errores.append("El teléfono debe contener solo números y tener al menos 8 dígitos")
    
    if errores:
        messagebox.showerror("Errores", "\n".join(errores))
    else:
        messagebox.showinfo("Éxito", "Formulario enviado correctamente")
        # Aquí podrías guardar los datos en una base de datos o archivo
        print(f"Nombre: {nombreS}")
        print(f"Email: {email}")
        print(f"Fecha de Nacimiento: {fecha_nac}")
        print(f"Teléfono: {telefono}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("400x300")

# Configurar grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="we")

tk.Label(ventana, text="Correo electrónico:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_email = tk.Entry(ventana)
entry_email.grid(row=1, column=1, padx=5, pady=5, sticky="we")

tk.Label(ventana, text="Fecha de nacimiento (DD/MM/AAAA):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_fecha = tk.Entry(ventana)
entry_fecha.grid(row=2, column=1, padx=5, pady=5, sticky="we")

tk.Label(ventana, text="Teléfono:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=3, column=1, padx=5, pady=5, sticky="we")

# Botón de envío
btn_enviar = tk.Button(ventana, text="Enviar", command=validar_formulario)
btn_enviar.grid(row=4, column=1, pady=10, sticky="e")

# Ejecutar la aplicación
ventana.mainloop()
