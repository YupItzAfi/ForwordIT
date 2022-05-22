import mysql.connector as sql

mydb = sql.connect(host="127.0.0.1", user="root",
                   password="As3eRT0P_", database="testdb")

cursur = mydb.cursor()

cursur.execute(
    "CREATE TABLE random (id int PRIMARY KEY AUTO_INCREMENT, user VARCHAR(50))")

cursur.execute("SELECT * FROM random")
