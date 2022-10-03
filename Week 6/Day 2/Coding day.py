import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'admin'
DATABASE = 'restaurantbusiness'

class MenuItem():

    def run_query(self,query):
        connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD,  dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def __init__(self,prices,names):
        self.prices = prices
        self.names = names

    def save(self):
        #try:
            query = f"INSERT INTO restaurant(names, prices) VALUES ('{self.names}',{self.prices})"
            self.run_query(query)
    def delete(self):
        #try:
            query = f"DELETE FROM restaurant WHERE (names, prices) = ('{self.names}',{self.prices})"
            self.run_query(query)
    def update(self):
        #try:
            query = f"UPDATE restaurant SET names = 'Okok', prices = 5000"
            self.run_query(query)
item = MenuItem(2000, 'ERU')
item.update()