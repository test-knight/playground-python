import unittest

# This is the function you want to test
def add(x, y):
    return x + y

class TestAdditionFunction(unittest.TestCase):

    def test_add(self):
        # Test positive numbers
        self.assertEqual(add(2, 2), 4)

        # Test negative numbers
        self.assertEqual(add(-1, -1), -2)

        # Test positive and negative numbers
        self.assertEqual(add(3, -3), 0)
    
    def test_integers(self):
        self.assertTrue(type(add(1,2) is int))

if __name__ == '__main__':
    unittest.main()
