import sys

#get user arguments and allow user to parse file name directly
user_args = sys.argv
print(user_args)

from time import time
import pandas as pd
import requests

#modules to handle some database operations
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import String, Integer, Column
from sqlalchemy import create_engine

import psycopg2

#database URI
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:qweaz@127.0.0.1:5432/copia'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


while True:
    #Create connection to database
    try:
        conn = psycopg2.connect(SQLALCHEMY_DATABASE_URL)
        cursor = conn.cursor()
        print('Database connected successfully')
        break

    except Exception as e:
        print('connection failed')
        print("Error: ", e)
        time.sleep(2)


#Model to handle table creation
class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    response = Column(String, nullable=False)


#Create all tables defined
Base.metadata.create_all(bind=engine)


#The main function to perform the tasks
def main():
    #Get the dataset
    dataset = pd.read_csv(str(user_args[1]))
    print(dataset)
    print(dataset.head())

    #define a list for ease of appending
    my_list = list()
    for index, row in dataset.iterrows():
        my_list.append(row.to_dict())

    print(my_list)

    #loop through the dictionaries in a list
    for item in my_list:
        #create a HTTP request [post to be specific]
        r = requests.post('http://httpbin.org/post', data=item)
        print(r)
        print(r.reason)

        #Insert data into the database; not the method used - this reduces sql injection cases
        #we also added the status_code as respose
        cursor.execute(""" INSERT INTO users (first_name, second_name, age, response) VALUES (%s, %s, %s, %s)
                        RETURNING * """, (item['first_name'], item['second_name'], item['Age'], r.status_code))
        
        #commit changes to the database
        conn.commit()
        print('1 recorded added successfully')
    conn.close()

 
main()
