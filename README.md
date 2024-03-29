# Database Query Builder 

- A library that serves as a means of connecting to a database and executing sql statements.

### Installation 😀📚
> ````pip install db_querybuilder````

## Get started 
How to use  **Database Query Builder**

It is very important to make the connection to the database that we are going to use.

## New Version updated
- New updated version ***0.2.0***

- Now with Sqlite integration. If you will use the sqlite integration, I invite you to read the official sqlite documentation, to see the types of data that it allows to use.

````python
from db_querybuilder import DatabaseQueryBuilder

class TestUser():
    def __init__(self) -> None:
        self.id = -1
        self.first_name = 'Jhon'
        self.last_name = 'Doe'


if __name__ == '__main__':
    db = DatabaseQueryBuilder(db_user='root',db_password='',db_database='test',db_port=3306)

    # Query to json
    query = db.setTable('test_data').query().where(clausule='id',parameter=1).toJson()
    print(query)

    # Query select
    query = db.select(['id','first_name']).from_('test_data').where('email','emaffini0@mlb.com').results()
    print(query)

    # Insert data with attributes object
    user = TestUser()
    query = db.insert(table='test_data',object=user)
    print(query)

    # Intregration with sqlite
    # New version with sqlite queries

    dbSqlite = DatabaseQueryBuilder(db_database='./db/hmi_creatio', driver= DatabaseDrivers.DRIVER_SQLITE.value)
    dbSqlite.setTable('test_data')


    query = dbSqlite.createTable(columns = ['id integer primary key autoincrement','name varchar(40)']).insert(fields=['id','name'],values=[1,'Jhon Doe'])
    print(query)

    query = dbSqlite.select(fields=['id','name']).toJson()
    print(query)

````



