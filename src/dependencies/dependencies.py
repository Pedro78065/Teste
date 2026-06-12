from src.models.mysql_models import table_user, createDB_pizza

def pegar_table():
    createDB_pizza()
    table_user()