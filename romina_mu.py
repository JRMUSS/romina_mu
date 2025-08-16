import os
import tkinter as tk
from tkinter import messagebox

class Pelicula:
    def __init__(self, titulo):
        titulo_limpio = titulo.strip()
        if not titulo_limpio:
            raise ValueError("El título de la película no puede estar vacío.")
        self.__titulo = titulo_limpio

    @property
    def titulo(self):
        return self.__titulo

    def __str__(self):
        return self.__titulo

class CatalogoPelicula:
    def __init__(self, nombre):
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise ValueError("El nombre del catálogo no puede estar vacío.")
        self.nombre = nombre_limpio
        self.ruta_archivo = self.nombre + ".txt"
        try:
            open(self.ruta_archivo, "x", encoding="utf-8").close()
        except FileExistsError:
            pass

    def agregar(self, pelicula):
        with open(self.ruta_archivo, "a", encoding="utf-8") as f:
            f.write(pelicula.titulo + "\n")

    def listar(self):
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                return [linea.strip() for linea in f if linea.strip()]
        except FileNotFoundError:
            return []

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            return True
        return False

# Interfaz gráfica mejorada
class InterfazCatalogo:
    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.ventana = tk.Tk()
        self.ventana.title("Catálogo de Películas")

        tk.Label(self.ventana, text="Gestor de Catálogo de Películas", font=("Arial", 14, "bold")).pack(pady=10)

        self.entry_pelicula = tk.Entry(self.ventana, width=40)
        self.entry_pelicula.pack(pady=5)

        tk.Button(self.ventana, text="Agregar Película", width=30, command=self.agregar_pelicula).pack(pady=5)
        tk.Button(self.ventana, text="Eliminar Catálogo", width=30, command=self.eliminar_catalogo).pack(pady=5)
        tk.Button(self.ventana, text="Salir", width=30, command=self.ventana.destroy).pack(pady=5)

        self.listbox = tk.Listbox(self.ventana, width=50)
        self.listbox.pack(pady=10)
        self.actualizar_lista()

        self.ventana.mainloop()

    def agregar_pelicula(self):
        titulo = self.entry_pelicula.get().strip()
        if titulo:
            try:
                pelicula = Pelicula(titulo)
                self.catalogo.agregar(pelicula)
                self.entry_pelicula.delete(0, tk.END)
                self.actualizar_lista()
                messagebox.showinfo("Éxito", f"Película '{pelicula.titulo}' agregada.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for p in self.catalogo.listar():
            self.listbox.insert(tk.END, p)

    def eliminar_catalogo(self):
        if self.catalogo.eliminar():
            self.actualizar_lista()
            messagebox.showinfo("Éxito", "Catálogo eliminado correctamente.✅")
        else:
            messagebox.showwarning("Aviso", "No existe un catálogo para eliminar.⚠️")

# Programa principal
def main():
    nombre_catalogo = input("Ingresa el nombre del catálogo de películas 🎞️: ").strip()
    try:
        catalogo = CatalogoPelicula(nombre_catalogo)
    except ValueError as e:
        print(f"Error: {e}")
        return

    modo = input("¿Quieres usar la versión gráfica (g)🕹️ o consola (c)✨? ").strip().lower()
    if modo == "g":
        InterfazCatalogo(catalogo)
    else:
        print("Modo consola aún disponible en el código original.")

if __name__ == "__main__":
    main()
