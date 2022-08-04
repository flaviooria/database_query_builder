import unittest
from db_querybuilder.databasequerybuilder import *

class TestUser():
    def __init__(self) -> None:
        self.id = -1
        self.first_name = 'Jhon'
        self.last_name = 'Doe'


class DatabaseQueryBuilderTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.db = DatabaseQueryBuilder(db_user='root',db_password='',db_database='test',db_port=3306)
        return super().setUp()

    def test_toJson(self):
        # Query to json
        query = self.db.setTable('test_data').query().where(clausule='id',parameter=1,operator='=').toJson()
        self.assertEqual(query,'[{"id": 1, "first_name": "Edouard", "last_name": "Maffini", "email": "emaffini0@mlb.com"}]')

    def test_toJson_error(self):
        # Query to json
        query = self.db.setTable('test_data').query().where(clausule='id',parameter=2).toJson()
        self.assertNotEqual(query,'[{"id": 1, "first_name": "Edouard", "last_name": "Maffini", "email": "emaffini0@mlb.com"}]')

    def test_select(self):
        query = self.db.select(['id','first_name']).from_('test_data').where('email','emaffini0@mlb.com').results()
        self.assertEqual(query,[(1,'Edouard')])

    def test_select_error(self):
        query = self.db.select(['id','first_name']).from_('test_data').where('email','emaffini0@mlb.com').results()
        self.assertNotEqual(query,[(1,'Robert')])

    def test_insert(self):
        # Insert data with fields and parameters
        query = self.db.insert(table='test_data',fields=['first_name'],values=['example_name'])
        self.assertEqual(query,query)

    def test_insert_error(self):
        # Insert data with fields and parameters
        query = self.db.insert(table='test_data',fields=['first_name'],values=['example_name'])
        self.assertNotEqual(query,-1)

    def test_insert_object(self):
        # Insert data with attributes object
        user = TestUser()
        query = self.db.insert(table='test_data',object=user)
        self.assertEqual(query,query)

    def test_insert_object_error(self):
        # Insert data with attributes object
        user = TestUser()
        query = self.db.insert(table='test_data',object=user)
        self.assertNotEqual(query,-1)

    def test_insert_many_data(self):
        # Insert many data
        query = self.db.insertMany(table='test_data',fields=['first_name'],values=['EXAMPLE1','EXAMPLE2','EXAMPLE3'])
        self.assertNotEqual(query,None)

    def test_insert_many_data_error(self):
        # Insert many data
        query = self.db.insertMany(table='test_data',fields=['name'],values=['EXAMPLE1','EXAMPLE2','EXAMPLE3'])
        self.assertEqual(query,None)

    def test_update(self):
        # Update data
        query = self.db.update(table='test_data',fields=['first_name'],values=[('Example Update')],clausule='first_name',parameter='example_name')
        print(query)
        value = True if not query == None else False
        self.assertTrue(query,value)


    def test_update_error(self):
        # Update data
        query = self.db.update(table='test_data',fields=['name'],values=[('Example Update')],clausule='first_name',parameter='example_name')
        print(query)
        value = True if not query == None else False
        self.assertFalse(query,value)
        
    def test_delete(self):
        # Delete data
        query = self.db.delete(table='test_data',clausule='first_name',parameter='Jhon')
        value = True if not query == None else False
        self.assertTrue(query,value)

    def test_delete_error(self):
        # Delete data
        query = self.db.delete(table='test_data',clausule='name',parameter='Example Update')
        value = True if not query == None else False
        self.assertFalse(query,value)

if __name__ == '__main__':
    unittest.main()