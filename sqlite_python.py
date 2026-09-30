import sqlite3
connection = sqlite3.connect("clientes.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS cliente;")



cursor.execute("""CREATE TABLE cliente ( id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(100), cidade varchar(100)); """)

cursor.execute("""INSERT into cliente values (1, 'Pietro', 'Ribeirão das Neves'),
                                             (2, 'Camila', 'Ribeirão Preto'),
                                             (3, 'Bernardo', 'Piratininga');""")

connection.commit()
cursor.execute("select *  from cliente;")
print(cursor.fetchall())

  