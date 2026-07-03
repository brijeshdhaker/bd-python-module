import unittest
from com.example.utils.GmailProcessor import GmailProcessor
from email.message import EmailMessage

class TestGmailProcessor(unittest.TestCase):

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
        # 1. Create the Gmail Processor Service
        GmailProcessor()

    #
    def test_init(self):
        self.assertIsNotNone(GmailProcessor.service, "Pass")

    #
    def test_send(self):

        # 2. Create the email content
        msg = EmailMessage()
        msg['Subject'] = "Testing Python Email"
        msg['From'] = "brijeshdhaker@gmail.com"
        msg['To'] = "brijeshdhaker@gmail.com"
        msg.set_content("This is a test email sent from a Python script!")

        result = GmailProcessor.send(msg)

        self.assertIsNotNone(result, "Pass")