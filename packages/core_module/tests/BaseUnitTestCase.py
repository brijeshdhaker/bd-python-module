import unittest
import sys

# tomllib is native to Python 3.11+. Use tomli for older versions.
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

class BaseUnitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("packages/core_module/tests/config.toml", "rb") as f:
            cls.config = tomllib.load(f)