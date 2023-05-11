import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def test_response(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'cos', 'num_2': 45, 'num_3': 3, 'num_4': 'on'})
            self.assertEqual(response.status_code, 200)

    def test_sin(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'sin', 'num_2': 45, 'num_3': 3, 'num_4': 'on'})
            self.assertIn(b'0.707', response.data)

    def test_cos(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'cos', 'num_2': 60, 'num_3': 3, 'num_4': 'on'})
            self.assertIn(b'0.5', response.data)

    def test_tan(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'tan', 'num_2': 45, 'num_3': 3, 'num_4': 'on'})
            self.assertIn(b'1', response.data)

    def test_ctg(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'ctg', 'num_2': 0, 'num_3': 4, 'num_4': 'None'})
            self.assertIn(bytes("нет решения", "utf-8"), response.data)

    def test_random_name(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'abc', 'num_2': 0, 'num_3': 4, 'num_4': 'None'})
            self.assertIn(bytes("такой функции нет", "utf-8"), response.data)
            
if __name__ == '__main__':
    unittest.main()