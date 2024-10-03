import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', # or '127.0.0.1'
    port='3306',
    user='root',
    password='Heu3BecTeH044',     
    # database = 'python15'
    database = 'sakila'
)

mycursor = mydb.cursor()
print(mycursor) #(nothing executed)
# mycursor.execute('SHOW DATABASE')
# print(mycursor) #show databases

# for db in mycursor:
#     print(db)

# mycursor = mydb.cursor()
# print(mycursor)
# mycursor.execute('CREATE TABLE student (name VARCHAR(255), age INTEGER(2));')

# user = ('Bob', 20)
# sql_formula = f'INSERT INTO student (name, age) VALUES ("{user[0]}", {user[1]})'
# mycursor.execute(sql_formula)

# user = ('Mary', 30)
# sql_formula = f'INSERT INTO student (name, age) VALUES ("{user[0]}", {user[1]})'
# mycursor.execute(sql_formula)

# sql_formula = 'INSERT INTO student (name, age) VALUES (%s, %s)'

# user = ('Sarah', 40)
# mycursor.execute(sql_formula, user)

# users = [('Samanta', 29), ('Mary', 31), ('Serjo', 45)]
# mycursor.executemany(sql_formula, users)

# mydb.commit()

mycursor.execute('SELECT * FROM actor;')

for x in range(3):
    result = mycursor.fetchone()
print(result)
