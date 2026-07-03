from com.example.models.Order import Order
import unittest
from faker import Faker

class TestOrder(unittest.TestCase):

    def test_wrap(self):

        name = "Brijesh"
        lname = "Dhaker"
        address =  { 'country': 'India', 'city': 'Pune', 'area': ["Kharadi", "Hadapsar","Whagoli"]}

        def _print(**kwargs):
            for key, value in kwargs.items():
                print(f"  {key}: {value}  {type(value)}")
                
        
        _print(**address)
    

        #object = Order(address=address)

        #result = object._wrap(address)

        # self.assertEqual(obj.address.country,'Country A')  #  Country A
        # self.assertEqual(obj.address.codes, [1, 2, 3])  #  [1, 2, 3]
        # self.assertEqual(obj.name,'bobbyhadz')  #  bobbyhadz
        # assert False



        # Calling the function with different keyword arguments
        # display_user_info(name="Alice", age=30, city="New York")
        # print("\n---")
        # display_user_info(username="bob_smith", email="bob@example.com", occupation="Engineer", country="Canada")
        # print("\n---")
        # display_user_info(product_id="P123", price=99.99)


