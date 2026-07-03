import unittest
from com.example.utils.MysqlProcessor import MysqlProcessor

class TestMysqlProcessor(unittest.TestCase):

    #
    @classmethod
    def setUpClass(cls):
        cls.clsVar = 1
        print(f"cls.clsVar :: {cls.clsVar}")
        
    
    @classmethod
    def tearDownClass(cls):
        cls.clsVar = 0
        print(f"cls.clsVar :: {cls.clsVar}")
        
    
    #
    def setUp(self):
        self.processor = MysqlProcessor()

        cnt = self.processor.execute(sql="DROP TABLE IF EXISTS `TEST_CUSTOMERS`")

        _sql = """CREATE TABLE IF NOT EXISTS `TEST_CUSTOMERS` (
                    ID INT NOT NULL AUTO_INCREMENT,
                    NAME VARCHAR(15) NOT NULL,
                    AGE INT NOT NULL,
                    ADDRESS VARCHAR(25),
                    SALARY FLOAT(10, 2),
                    PRIMARY KEY(ID)
                );"""
        self.processor.execute(sql=_sql)

        _sql = "INSERT INTO `TEST_CUSTOMERS` (`NAME`, `AGE`, `ADDRESS`, `SALARY`) VALUES (%s, %s, %s, %s)"
        _val = [
            ('Ramesh', '32', 'Ahmedabad', 2000),
            ('Khilan', '25', 'Delhi', 1500),
            ('Kaushik', '23', 'Kota', 2500),
            ('Chaitali', '26', 'Mumbai', 6500),
            ('Hardik','27', 'Bhopal', 8500),
            ('Komal', '22', 'Hyderabad', 9000),
            ('Muffy', '24', 'Indore', 5500)
        ]
        cnt = self.processor.insert(sql=_sql, values=_val)

    #
    def tearDown(self):
        cnt = self.processor.execute(sql="DROP TABLE IF EXISTS `TEST_CUSTOMERS`")
        self.assertTrue(cnt == 0)
        self.processor.close()

    #
    def test_init(self):
        self.assertIsNotNone(self.processor.connection, "Pass")

    #
    def test_fetchOne(self):
        
        _result = self.processor.fetchOne(sql="select * from `TEST_CUSTOMERS`")
        
        #self.assertTrue(isinstance(_result, dict)) 
        #for row in results:
        #    print(row)
        self.assertIsNotNone(_result, "Pass")
        #self.assertTrue(len(_result) > 0)
        

    #
    def test_fetchOneAsDict(self):

        _result = self.processor.fetchOne(sql="select * from `TEST_CUSTOMERS`", isdict=True)
        
        self.assertTrue(isinstance(_result, dict)) 
        self.assertIsNotNone(_result, "Pass")
        #self.assertTrue(len(_result) > 0)
    #
    def test_fetchAll(self):
        results = self.processor.fetchAll(sql="select * from `TEST_CUSTOMERS`")
        #for row in results:
        #    print(row)
        self.assertIsNotNone(results, "Pass")
        self.assertTrue(len(results) > 0)

    #
    def test_insert(self):
        _sql = "INSERT INTO `TEST_CUSTOMERS` (`NAME`, `AGE`, `ADDRESS`, `SALARY`) VALUES (%s, %s, %s, %s)"
        _val = [
            ('Ramesh', '32', 'Ahmedabad', 2000),
            ('Khilan', '25', 'Delhi', 1500),
            ('Kaushik', '23', 'Kota', 2500),
            ('Chaitali', '26', 'Mumbai', 6500),
            ('Hardik','27', 'Bhopal', 8500),
            ('Komal', '22', 'Hyderabad', 9000),
            ('Muffy', '24', 'Indore', 5500)
        ]
        cnt = self.processor.insert(sql=_sql, values=_val)
        self.assertEqual(cnt,7)

    #
    def test_insertBlank(self):
        _sql = "INSERT INTO `TEST_CUSTOMERS` (`NAME`, `AGE`, `ADDRESS`, `SALARY`) VALUES (%s, %s, %s, %s)"
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            self.processor.insert(sql=_sql, values=None)

    #
    def test_insertBlankSql(self):
        _sql = ""
        _values = [
            ('Ramesh', '32', 'Ahmedabad', 2000),
        ]
        # check that s.split fails when the separator is not a string
        with self.assertRaises(Exception):
            self.processor.insert(sql=_sql, values=_values)

    #
    def test_executeDelete(self):
        cnt = self.processor.execute(sql="DELETE FROM `TEST_CUSTOMERS` WHERE NAME = 'Muffy'")
        self.assertTrue(cnt > 0)

if __name__ == '__main__':
    unittest.main()