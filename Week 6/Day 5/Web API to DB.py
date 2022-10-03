import psycopg2
import requests
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'admin'
DATABASE = 'API'

class API():

    def run_query(self,query):
        connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD,  dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def __init__(self,name,capital,region):
        self.name = name
        self.capital = capital
        self.region = region

    def countries(self):
        #try:
            query = f"INSERT INTO API(name,capital,region) VALUES ('{self.name}','{self.capital}','{self.region}')"
            self.run_query(query)

api =  API()
api.countries()

response = requests.get("https://restcountries.com/v3.1/all")
jun = response.json()
print(jun['name','capital','region'])




