import unittest

from tp import *

class UserTests(unittest.TestCase):
    def test_init(self):
        user = User("Pablo", "pablo@pablo.com")
        self.assertEqual("Pablo", user.name)
        self.assertEqual("pablo@pablo.com", user.email)

if __name__ == "__main__":
    unittest.main()
