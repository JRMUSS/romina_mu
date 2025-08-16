from tkinter import *
from tkinter import messagebox
import os

# --- Clase Pelicula ---
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # atributo privado

    def get_nombre(self):
        return self.__nombre

# --- Clase CatalogoPelicula ---
class CatalogoPelicula:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"

    def agregar(self, pelicula):
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(pelicula.get_nombre() + "\n")
        messagebox.showinfo("Éxito", f"'{pelicula.get_nombre()}' agregada al catálogo.")

    def listar(self):
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                return [linea.strip() for linea in archivo]
        except FileNotFoundError:
            return []

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            messagebox.showinfo("Éxito", f"Catálogo '{self.nombre}' eliminado.")
        else:
            messagebox.showwarning("Advertencia", "No existe el catálogo para eliminar.")

# --- Crear catálogo ---
catalogo = CatalogoPelicula("peliculas")  # <- instancia del catálogo

# --- Funciones de la interfaz ---
def agregar_pelicula():
    nombre = entry_nombre.get().strip()
    if nombre == "":
        messagebox.showwarning("Error", "Debe ingresar un nombre de película")
        return
    pelicula = Pelicula(nombre)
    catalogo.agregar(pelicula)
    actualizar_lista()
    entry_nombre.delete(0, END)

def actualizar_lista():
    lista_peliculas.delete(0, END)
    for p in catalogo.listar():
        lista_peliculas.insert(END, p)

def eliminar_catalogo():
    catalogo.eliminar()
    actualizar_lista()

# --- Interfaz gráfica ---
root = Tk()
root.title("Catálogo de Películas")
root.geometry("500x400")  # tamaño de ventana
root.configure(bg="#2C3E50")  # color de fondo

# Estilos de texto
font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 11, "bold")
font_listbox = ("Helvetica", 12)

Label(root, text="Nombre de la película:", bg="#2C3E50", fg="white", font=font_label).pack(pady=10)
entry_nombre = Entry(root, width=40, font=font_entry)
entry_nombre.pack(pady=5)

Button(root, text="Agregar Película", command=agregar_pelicula, bg="#27AE60", fg="white", font=font_button).pack(pady=5)
Button(root, text="Actualizar Lista", command=actualizar_lista, bg="#2980B9", fg="white", font=font_button).pack(pady=5)
Button(root, text="Eliminar Catálogo", command=eliminar_catalogo, bg="#C0392B", fg="white", font=font_button).pack(pady=5)

lista_peliculas = Listbox(root, width=50, height=10, font=font_listbox)
lista_peliculas.pack(pady=15)
actualizar_lista()

root.mainloop()
