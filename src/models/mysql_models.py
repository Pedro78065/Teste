import mysql.connector

host = "localhost"
user = "root"
password = ""
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
            

def table_user():
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        cursor = conexao.cursor()
        comando = f"""create table if not exists users(
        id int auto_increment,
        nome varchar(50) not null,
        email varchar(255) not null unique,
        senha varchar(255) not null,
        ativo boolean default false,
        admin boolean default false,
        primary key(id)
        )engine = innoDB charset = utf8mb4;"""
        cursor.execute(comando)
        conexao.commit()
    except mysql.connector.Error as e:
        print(f"Erro:{e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def table_pedido():
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        cursor = conexao.cursor()
        comando = f"""create table if not exists orders(
        id int auto_increment,
        status enum('pendente','cancelado','finalizado') default 'pendente' not null,
        usuario int not null,
        preco decimal(10, 2) default '0.00' not null,
        primary key(id),
        foreign key(usuario) references users(id)
        )engine = innoDB charset utf8mb4;"""
        cursor.execute(comando)
        conexao.commit()
    except mysql.connector.Error as e:
        print(f"Erro:{e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def table_ItensPedido():
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        cursor = conexao.cursor()
        comando = f"""create table if not exists ItensPedidos(
        id int auto_increment,
        quantidade int,
        sabor varchar(35),
        tamanho varchar(30),
        preco_unitario decimal(10,2),
        pedido int,
        primary key(id),
        foreign key(pedido) references pedidos(id)
        )engine = innoDB charset = utf8mb4;"""
        cursor.execute(comando)
        conexao.commit()
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    finally:
        if conexao:
            conexao.close()
        if cursor:
            cursor.close()


def insert_user(user_name, user_email, user_password, user_ativo = False, user_admin = False):
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        cursor = conexao.cursor()
        comando = f"""insert into users
        (id, nome, email, senha, ativo, admin)
        values
        (defualt, %s, %s, %s, %s, %s);"""
        dados = (user_name, user_email, user_password, user_ativo, user_admin)
        cursor.execute(comando, dados)
        conexao.commit()
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    finally:
        if conexao:
            conexao.close()
        if cursor:
            conexao.close()


def select_user_fromEmail(user_email):
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        cursor = conexao.cursor(dictionary = True)
        comando = f"""select * from users
        where email = %s;"""
        dados = (user_email,)
        cursor.execute(comando, dados)
        read = cursor.fetchone()
        return read
    except mysql.connector.Error as e:
        print(f"Error:{e}")
    finally:
        if conexao:
            conexao.close()
        if cursor:
            conexao.close()