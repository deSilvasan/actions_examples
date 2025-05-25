import unittest
from db import get_mysql_version

class TestMySQLVersion(unittest.TestCase):

    def test_get_mysql_version(self):
        version = get_mysql_version()
        self.assertIsInstance(version, str)
        self.assertRegex(version, r'^\d+\.\d+\.\d+')  # z.B. 8.0.33

if __name__ == "__main__":
    unittest.main()
