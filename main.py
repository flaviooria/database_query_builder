from db_querybuilder import DatabaseQueryBuilder
from db_querybuilder import DatabaseDrivers

class TestUser():
    def __init__(self) -> None:
        self.id = -1
        self.first_name = 'Jhon'
        self.last_name = 'Doe'


if __name__ == '__main__':
    dbMySql = DatabaseQueryBuilder(db_database='db_test',driver= 'MYSQL').setHost('localhost').setUserAndPassword(user='root',password='').setPort(3306).setTable('test_data')

    # Query to json
    query = dbMySql.select().where(clausule='id',parameter=1).toJson()
    print(query)

    query = dbMySql.select(fields=['id','first_name']).where('email','emaffini0@mlb.com').results()
    print(query)

    # Insert data with fields and parameters
    query = dbMySql.insert('test_data',fields=['first_name'],values=['example_name'])
    print(query)

    # Insert data with attributes object
    user = TestUser()
    query = dbMySql.insert('test_data',object=user)
    print(query)

    # Insert many data
    query = dbMySql.insertMany(table='test_data',fields=['first_name'],values=['EXAMPLE1','EXAMPLE2','EXAMPLE3'])
    print(query)

    # Update data
    query = dbMySql.update(table='test_data',fields=['first_name'],values=[('Example Update')],clausule='first_name',parameter='example_name')
    print(query)

     # Delete data
    query = dbMySql.delete(table='test_data',clausule='first_name',parameter='Example Update')
    print(query)

    # New version with sqlite queries

    dbSqlite = DatabaseQueryBuilder(db_database='./db/hmi_creatio', driver= DatabaseDrivers.DRIVER_SQLITE.value)
    dbSqlite.setTable('test_data')


    query = dbSqlite.createTable(columns = ['id integer primary key autoincrement','name varchar(40)']).insert(fields=['id','name'],values=[1,'Jhon Doe'])
    print(query)

    query = dbSqlite.select(fields=['id','name']).toJson()
    print(query)
