import unittest
from source.main.DBDriver import DBDriver


class DBDriverTest(unittest.TestCase):
    """Test suites for class DBDriver."""

    params = {
        'dbname': 'sql_full_man',
        'host': 'localhost',
        'password': 'postgresrootpass',
        'port': 5432,
        'user': 'postgres'
    }

    # Actions before each test.
    def setUp(self):
        self.driver = DBDriver(DBDriverTest.params)

    # tests delete(query=''). Successful execution.
    def testDelete(self):
        query = "delete from offices where city='New York'"
        result = self.driver.insert(query)
        self.assertEqual(1, result)

    # tests executeSql(query=''). Successful execution.
    def testExecuteSqlSuccess(self):
        query = 'select count(*) from offices'
        result = self.driver.executeSql(query)
        self.assertTrue(result['rows'][0][0] > 0)

    # tests executeSql(query=''). Exception threw due empty query string.
    def testExecuteSqlThrowsEmptyQuery(self):
        self.assertRaises(Exception, self.driver.executeSql, '')

    # tests insert(query=''). Successful execution.
    def testInsertSuccess(self):
        query = """insert into offices (office, city, region, mgr, target, sales) 
        values (23, 'San Diego', 'Western', 108, 660000.0, 0.0)"""
        result = self.driver.insert(query)
        self.assertEqual(1, result)

    # tests isConnected(). False returned.
    def testIsConnectedReturnsFalse(self):
        self.assertFalse(self.driver.isConnected())

    # tests setConnection(). Successful execution.
    def testSetConnectionSuccess(self):
        self.driver.setConnection()
        self.assertTrue(self.driver.isConnected())

    # tests select(query=''). Successful execution.
    def testSelectSuccess(self):
        query = 'select * from offices'
        result = self.driver.select(query)
        self.assertTrue(result.__len__())

    # tests update(query=''). Successful execution.
    def testUpdate(self):
        query = "update offices set mgr=105 where city='Denver'"
        result = self.driver.update(query)
        self.assertEqual(1, result)

    # Actions after each test.
    def tearDown(self):
        self.driver.executeSqlScript('schema_PostgreSQL.sql')
        self.driver.executeSqlScript('schema_inserts_PostgreSQL.sql')
        self.driver.executeSqlScript('chapter_7_boys_girls.sql')
        self.driver.close()
