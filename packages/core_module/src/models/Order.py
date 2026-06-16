

class Order(object):

    # The *args will give you all positional arguments as a tuple:
    # The **kwargs will give you all keyword arguments as a dictionary:

    # *args: Non-keyword (positional) arguments
    # **kwargs: Keyword arguments
    
    #
    def __init__(self, **kwargs):
        # for name, value in kwargs.items():
        #     setattr(self, name, self._wrap(value))

        for key, value in kwargs.items():
            if isinstance(value, dict):
                self.__dict__[key] = Order(**value)
            else:
                self.__dict__[key] = value

    #
    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Order(**value) if isinstance(value, dict) else value
        
    
    def display_order_info(self, **order_details):
        """
        This function takes an arbitrary number of keyword arguments 
        and prints them as user details.
        """
        print("Order Details:")
        for key, value in order_details.items():
            print(f"  {key.replace('_', ' ').capitalize()}: {value}")
