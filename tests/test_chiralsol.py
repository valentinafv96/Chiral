import unittest
from chiral import chiralsol


class Test_chiralsolone(unittest.TestCase):
    def test__working(self):
        self.assertEqual(chiralsol.paralelo(5, 1000000, 9, 0, 30, solution),
                         11, True)

class Test_chiralsoltwo(unittest.TestCase):
    def test__working(self):
        self.assertEqual(chiralsol.paralelo(6, 1000000, 9, 0, 30, solution),
                         112, True)

if __name__ == '__main__':
    unittest.main()
