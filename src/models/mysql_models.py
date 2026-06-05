import mysql.connector

host = "localhost"
user = "pedro"
password = "123456"
database = "db_pizza"

def createDB_pizza():
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )
        cursor = conexao.cursor()
        comando = f"""create database if not exists {database}
        charset utf8mb4
        collate utf8mb4_general_ci;"""
        cursor.execute(comando)
        conexao.commit()
        print(f"O db {database} foi criado com sucesso")
    except mysql.connector.Error as e:
        print(f"Erro:{e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            

