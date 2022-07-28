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

    query = db.select(['id','first_name']).from_('test_data').where('email','emaffini0@mlb.com').results()
    print(query)

    # Insert data with fields and parameters
    query = db.insert(table='test_data',fields=['first_name'],values=['example_name'])
    print(query)

    # Insert data with attributes object
    user = TestUser()
    query = db.insert(table='test_data',object=user)
    print(query)

    # Insert many data
    query = db.insertMany(table='test_data',fields=['first_name'],values=['EXAMPLE1','EXAMPLE2','EXAMPLE3'])
    print(query)

    # Update data
    query = db.update(table='test_data',fields=['first_name'],values=[('Example Update')],clausule='first_name',parameter='example_name')
    print(query)

     # Delete data
    query = db.delete(table='test_data',clausule='first_name',parameter='Example Update')
    print(query)
