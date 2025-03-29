import unittest


class c1(unittest.TestCase):
    def test_acc(self):
        str1 = 'admin hehe'
        self.assertEquals(str1.split('s', 1), ['admin hehe'])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())


if __name__ == '__main__':
    unittest.main()
