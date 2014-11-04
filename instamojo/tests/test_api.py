import unittest
from instamojo import Instamojo


class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = Instamojo(
            api_key='foo',
            auth_token='bar'
        )

    def test_debug(self):
        response = self.api.debug()

        self.assertEqual(isinstance(response, dict), True)
        self.assertEqual('success' in response, True)
        self.assertEqual(response.get('success'), False)
