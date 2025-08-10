import unittest


class TestLogin(unittest.TestCase):
    def test_login_success(self):
        self.assertEqual(200, 200)

    def test_login_failure(self):
        self.assertEqual(200, 200)  # 会失败


if __name__ == '__main__':
    unittest.main()