#
import unittest
from BaseUnitTestCase import BaseUnitTestCase

class MyTestCase(BaseUnitTestCase):
    def test_database_connection(self):
        db_url = self.config["test_env"]["database_url"]
        self.assertIsNotNone(db_url)

if __name__ == '__main__':
    unittest.main()        