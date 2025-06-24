import mysql.connector
from tkinter import *


class Database:
    def __init__(self):
        consumer_key = "krono"
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password=consumer_key,
          database="world"
        )

        mi_codigo_SQL = """
        SELECT *
        FROM city
        ORDER BY Population DESC
        """
        mycursor = mydb.cursor()
        mycursor.execute(mi_codigo_SQL)
        myresult = mycursor.fetchall()

        contador = 0
        self.resultados = []
        for row in myresult:
            if contador >= 10:
                break
            contador += 1
            self.resultados.append(row)

        mydb.close()


class Table:
    def __init__(self, root):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]

lst = Database().resultados

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()



