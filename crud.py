import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='bd_mercado' 
)

cursor = conexao.cursor()


#CREATE
nome_produto = "nescau cereal"
valor = 9
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
#Quando você EDITA o BD, o commit é necessário
conexao.commit()

#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
#Ler o BD
resultado = cursor.fetchall()
print(resultado)


#UPDATE
nome_produto = "nescau cereal"
valor = 6
comando = f'UPDATE vendas SET VALOR = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#DELETE
nome_produto = "nescau cereal"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


# É importante sempre fechar a conexão com o banco no fim do código
cursor.close()
conexao.close()
