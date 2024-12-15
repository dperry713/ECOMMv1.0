import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_graphql_endpoint(self):
        response = self.app.post('/graphql', json={'query': '{ allProducts { name } }'})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
