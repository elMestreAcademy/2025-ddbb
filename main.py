import mysql.connector
import tkinter as tk
from tkinter import ttk


class Database:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "krono",
            "database": "world"
        }

    def __fetch(self, query, params=None):
        try:
            with mysql.connector.connect(**self.config) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    return cursor.fetchall()

        except Exception as e:
            print(f"[ERROR] al ejecutar la consulta: {e}")
            raise e

    def cities(self, columns=None):
        if columns:
            projection = ", ".join(f"`{col}`" for col in columns)
        else:
            projection = "*"

        query = f"""
            SELECT {projection}
            FROM `city`
            ORDER BY `Population` DESC
        """

        return self.__fetch(query)


class App:
    def __init__(self, root):
        # columns = ("ID", "Name", "CountryCode", "District", "Population")
        columns = ("ID", "Name", "District", "Population")

        self.ventana()
        self.table(columns)
        self.loadData(columns)

    def ventana(self):
        root.title("Ciudades por población")
        root.geometry("800x400")  # ancho x alto inicial

        # Marco contenedor
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def table(self, columns):
        # Creamos Treeview
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)

        # Scrollbars vertical y horizontal
        vsb = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Layout
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        # Configuramos crecimiento de filas/columnas
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def loadData(self, columns):
        # Cargamos datos
        db = Database()
        resultados = db.cities(columns)
        for row in resultados:
            self.tree.insert("", tk.END, values=row)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
