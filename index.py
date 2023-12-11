import tkinter as tk
import sqlite3
import os

# Función para guardar los datos
def guardar_datos(nombre, apellido, edad):
  # Obtiene los datos del formulario

  nombre = nombre.get()
  apellido = apellido.get()
  edad = edad.get()

  # Inserta los datos en la base de datos
  cur.execute("INSERT INTO datos (nombre, apellido, edad) VALUES (?, ?, ?)", (nombre, apellido, edad))
  conn.commit()

  # Limpia los campos del formulario
  nombre.delete(0,-1)
  apellido.delete(0,-1)
  edad.delete(0,-1)

# Función para consultar los datos
def consultar_datos():
  # Obtiene los datos de la base de datos
  cur.execute("SELECT nombre, apellido, edad FROM datos")
  datos = cur.fetchall()

  # Muestra los datos en la consola
  for dato in datos:
    print(dato)

# Función para guardar los datos
def borrar_consulta():
  pass



# Crea la base de datos
conn = sqlite3.connect("database.db")

# Crea la tabla
cur = conn.cursor()

#verifica si la base de dato esta creada
ruta_archivo = os.path.join("database.db")

if os.path.exists(ruta_archivo) == False:
   cur.execute("""
    CREATE TABLE datos (
    nombre text,
    apellido text,
    edad integer
    )
        """)

# Crea la ventana principal
root = tk.Tk()
root.title("Formulario de datos")

# Crea los widgets del etiquetas
label_nombre = tk.Label(root, text="Nombre")
label_apellido = tk.Label(root, text="Apellido")
label_edad = tk.Label(root, text="edad")

# Crea los widgets del formulario
nombre = tk.Entry(root)
apellido = tk.Entry(root)
edad = tk.Entry(root)

# Crea los botones del formulario
boton_guardar = tk.Button(root, text="Guardar", command=guardar_datos(nombre,apellido,edad))
boton_consultar = tk.Button(root, text="Consultar", command=consultar_datos)
boton_borrar = tk.Button(root, text="Borrar", command=borrar_consulta)

# Coloca los widgets en la ventana
label_nombre.grid(row=0, column=0, padx=10, pady=10)
label_apellido.grid(row=1, column=0, padx=10, pady=10)
label_edad.grid(row=2, column=0, padx=10, pady=10)
nombre.grid(row=0, column=1, padx=10, pady=10)
apellido.grid(row=1, column=1, padx=10, pady=10)
edad.grid(row=2, column=1, padx=10, pady=10)
boton_guardar.grid(row=3, column=1, padx=10, pady=10)
boton_consultar.grid(row=4, column=1, padx=10, pady=10)
boton_borrar.grid(row=5, column=1, padx=10, pady=10)


# Inicia el bucle de eventos
root.mainloop()


