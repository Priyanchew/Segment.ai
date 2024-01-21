import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789',
    port='3306',
    database='login_info',
)
mycursor = mydb.cursor()
mycursor.execute('select * from users')
worker = mycursor.fetchall()

for user in worker:
    print(user)
    print('username',+ user[1])
    print('password'+ user[2])