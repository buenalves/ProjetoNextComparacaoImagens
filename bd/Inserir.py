import mysql.connector
from mysql.connector import Error

def inserir_banco(nome, uuid, phash):
    var = "('" + nome + "','" + uuid + "','" + phash + "')"

    try:
        con = mysql.connector.connect(host='localhost',database='dadosimagem', user = 'root', password = 'qfCSH5J6W&!&q')

        inserir_produtos = """INSERT INTO banco_imagem
                            (name_img, uuid, phash)
                            VALUES
                            """ + var

        cursor = con.cursor()
        cursor.execute(inserir_produtos)
        con.commit()
        print(cursor.rowcount, "registro insterido na tabela!")
        cursor.close()
    except Error as erro:
        print("Falha ao inserir: {}".format(erro))

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("conexão finalizada.")
