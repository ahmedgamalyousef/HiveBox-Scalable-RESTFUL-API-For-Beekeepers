# import unittest
# from app import app


# class TestApp(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_version(self):
#         response = self.app.get('/version')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json, {'version': 'v0.0.1'})

#     def test_metrics(self):
#         response = self.app.get('/metrics')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('average_temperature', response.data.decode())

#     def test_temperature(self):
#         response = self.app.get('/temperature')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('average_temperature', response.json)
#         self.assertIn('status', response.json)

#     def test_store(self):
#         response = self.app.post('/store')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json, {'status': 'Data stored successfully'})

#     def test_readyz(self):
#         response = self.app.get('/readyz')
#         self.assertIn(response.status_code, [200, 503])
#         self.assertIn('status', response.json)


# if __name__ == '__main__':
#     unittest.main()
