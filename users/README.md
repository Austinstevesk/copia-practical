# Users Module  

# Installation  
- Create a virtual environment using [Using Linux]  
```virtualenv venv -p python3.8```   
-Activate the virtual environment  
```source venv/bin/active```  
- Install dependencies   
```pip3 install -r requirements.txt```  

# Ensure you have the database ```copia``` ready and make sure the URI is correct  
  
# Running the code  
- Navigate to the directory and run  
```cd users/```  
```python3 users.py users.csv```  
  
# Code breakdown  
- sys.argv helps me capture user inputs and I get the second argument which is the data name    
- sqlalchemy helps me create tables instead of using normal 'CREATE TABLE users ... it is safer and constraints are easily parsed    
- conn is a variable holding the connection to the database using psycopg2 since we need it to insert data  
```We could have created a pydantic class but we are not creating an endpoint thus we use normal psycopg2```  
- dataset in the main function comes in as a python dataframe after being read from the csv  
- We convert the data to dictionary and append in a list for ease of iteration   
- We then loop through the data using the ```for item in mylist``` loop  
- We create requests and get the status_code which we psuh to the database as our response  
- We then add the data to the database using the ```INSERT ...``` statement  
- We commit the data using ```conn.commit()```  
- Finally we close the connection using ```conn.close()``` to avoid being connected forever. Note: This should be done after looping through all the elements. Otherwise we will close the connection after only one loop.  