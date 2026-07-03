import unittest
from core_module.utils.FileUtils import FileUtils

class TestFileUtils(unittest.TestCase):

    #
    def test_read(self):
        fileUtils = FileUtils()
        fileUtils.read("conf/avro/user-record.avsc")
        self.assertIsNotNone(2)

    #
    def test_delete(self):
        fileUtils = FileUtils()
        fileUtils.delete("conf/avro/user-record.avsc")
        

        
if __name__ == '__main__':
    unittest.main()