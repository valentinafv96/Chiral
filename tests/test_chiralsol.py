import unittest
from chiral import chiralsol


class Test_chiralsolone(unittest.TestCase):
    def test__working(self):
        self.assertEqual(chiralsol.paralelo(5),
                         11, True)


class Test_chiralsoltwo(unittest.TestCase):
    def test__working(self):
        self.assertEqual(chiralsol.paralelo(6),
                         112, True)


if __name__ == '__main__':
    unittest.main()
