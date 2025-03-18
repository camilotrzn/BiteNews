import sqlite3
from datetime import datetime

DATABASE_PATH = "src/backend/data/user_data/app.db"

def initialize_db():

    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        print(database_connection)

        query = 'select sqlite_version();'
        cursor.execute(query)

        result = cursor.fetchall()
        print('Version de SQLite = {}'.format(result))

        def initialize_tables():
            with open('src/backend/database/init_tables.sql', 'r') as file:
                sql_commands = file.read()

            cursor.executescript(sql_commands)
            print("Tablas verificadas con exito")

            database_connection.commit()

        initialize_tables()

        cursor.close()

    except sqlite3.Error as error:
        print("Ocurrio un error --> " + error)
    finally:
        database_connection.close()


def check_tables():
    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        tables =  cursor.fetchall()

        if tables:
            print("These tables are in the database:")
            for table in tables:
                print(table)

        else:
            print("No tables found")
    
    except sqlite3.Error as error:
        print("Error recuperando tablas --> " + error)

    finally:
        database_connection.close()


def print_tables(table):
    query = f"SELECT * FROM {table}"
    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        cursor.execute(query)
        output = cursor.fetchall()

        for row in output:
            print(row)

    except sqlite3.Error as error:
        print("Error mostrando noticias --> ",error)
    finally:
        database_connection.close()


def delete_table_data(table):
    query = f"DELETE FROM {table}"
    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        cursor.execute(query)

        database_connection.commit()

    except sqlite3.Error as error:
        print("Error borrando noticias --> ",error)

    finally:
        database_connection.close()

def new_news(elements):

    values_command = ",".join(f"'{element}'" for element in elements)

    query = f"INSERT INTO noticias (titulo, descripcion, publicador, fecha_publicacion, url, interaccion) VALUES ({values_command});"

    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        cursor.execute(query)
        database_connection.commit()

    except sqlite3.Error as error:
        print("Error guardando noticia --> ",error)


    finally:
        database_connection.close

def new_preferences(elements):

    values_command = ",".join(f"'{element}'" for element in elements)

    query = f"INSERT INTO preferencias (tema, nivel_interes) VALUES ({elements});"

    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        cursor.execute(query)
        database_connection.commit()

    except sqlite3.Error as error:
        print("Error guardando noticia --> ",error)

    finally:
        database_connection.close()

def new_interaction(elements):

    values_command = ",".join(f"'{element}'" for element in elements)

    query = f"INSERT INTO interacciones (news_id, tipo) VALUES ({elements});"

    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        cursor.execute(query)
        database_connection.commit()

    except sqlite3.Error as error:
        print("Error guardando noticia --> ",error)

    finally:
        database_connection.close()

def new_setting(elements):

    values_command = ",".join(f"'{element}'" for element in elements)

    query = f"INSERT INTO settings (clave, valor) VALUES ({elements});"

    try:
        database_connection = sqlite3.Connection(DATABASE_PATH)
        cursor = database_connection.cursor()

        cursor.execute(query)
        database_connection.commit()

    except sqlite3.Error as error:
        print("Error guardando noticia --> ",error)

    finally:
        database_connection.close()


if __name__ == "__main__":

    initialize_db()