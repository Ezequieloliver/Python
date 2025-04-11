import mysql.connector as mysql


# Conexão com Banco de Dados na Nuvem
conn = mysql.connect(
    host='roo27.h.filess.io',
    port=61002,
    user='testdb_skinskinit',
    password='21b3f71f7ce8420cc37c28e53a0f30e97e592ab5',
    database='testdb_skinskinit'
)

# Conexão Local
# conn = mysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='',
#     database='escola'
# )

def create_tables():
    with open('./sql/dump.sql', 'r') as file:
        sql = file.read()

    with conn.cursor() as cursor:
        cursor.execute(sql)


create_tables()