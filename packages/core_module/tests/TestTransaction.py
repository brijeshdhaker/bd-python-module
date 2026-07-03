import unittest
from core_module.models.Transaction import Transaction
from faker import Faker

class TestTransaction(unittest.TestCase):

    def test_random(self):
        for _ in range(100):
            pass

        transaction = Transaction.random()
        record_key = str(transaction.uuid)
        record_value = str(transaction.to_dict())
        # json.dumps() function converts a Python object into a json string.
        # record_value = json.dumps({'count': random.randint(1000, 5000)})
        print("{}\t{}".format(record_key, record_value))
        #assert False


    def test_dict_to_name(self):
        transaction = Transaction.random()
        # name = Transaction.dict_to_name(transaction)
        self.assertIsNotNone(transaction)


    def test_name_to_dict(self):
        transaction = Transaction.random()
        record_value = str(transaction.to_dict())
        self.assertIsNotNone(record_value)

    def test_to_dict(self):
        transaction = Transaction.random()
        record_value = str(transaction.to_dict())
        self.assertIsNotNone(record_value)


    def test_to_json(self):
        transaction = Transaction.random()
        record_value = str(transaction.to_json())
        self.assertIsNotNone(record_value)


    def test_to_delimited_text(self):
        transaction = Transaction.random()
        record_value = str(transaction.to_delimited_text("|"))
        self.assertIsNotNone(record_value)
