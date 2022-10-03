import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'admin'
DATABASE = 'dvdrental'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()
query = "INSERT INTO actor (first_name, last_name, last_update, number_oscars) VALUES('Matt','Damon','08/10/1970', 5);"
cursor.execute(query)
results = cursor.fetchall()
connection.close()
