from unittest.mock import patch
from unittest import TestCase, main
from .api import app as application
from .api import get_starships
import json

STARSHIPS_URL = '/starships'


class StarshipsTestCase(TestCase):
    """This class epresents the starships test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = application
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_starships_success(self):
        """Test fetching starships"""
        starships = get_starships()
        self.assertGreater(len(starships), 0)

    @patch('requests.get')
    def test_gest_starships_failure(self, status):
        """Test that an empty list is returned when the api is down"""
        status.return_value.ok = False
        starships = get_starships()
        self.assertEqual(len(starships), 0)

    def test_sort_starships(self):
        """Test that starships are fetched and sorted by hyperdrive_rating"""
        res = self.client().get(STARSHIPS_URL)
        data = json.loads(res.data)['data']
        self.assertGreater(len(data), 0)
        self.assertTrue(res.status_code, 200)
        prev_index = 0
        for i in range(1, len(data)):
            current_index = i
            prev_hyperdrive_rating = float(data[prev_index]['hyperdrive_rating'])
            current_hyperdrive_rating = float(data[current_index]['hyperdrive_rating'])
            self.assertLessEqual(prev_hyperdrive_rating, current_hyperdrive_rating)


if __name__ == "__main__":
    main()
