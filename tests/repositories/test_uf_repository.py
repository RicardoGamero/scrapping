import requests
from unittest import mock, TestCase
from app.repositories.uf_repository import UfRepository, PageError


class TestUfRepository(TestCase):

    def setUp(self):
        self.repo = UfRepository()

    def test_get_ufs_success(self):
        # arrange
        date = '01-01-2022'
        # act
        result = self.repo.get_ufs(date)
        # assert
        expected_result = '30.996,73'
        self.assertEqual(result, expected_result)

    @mock.patch('requests.get')
    def test_get_ufs_invalid_date(self, mock_get):
        # arrange
        date = '30/02/2022'

        # act/assert
        with self.assertRaises(ValueError):
            self.repo.get_ufs(date)

    @mock.patch('requests.get')
    def test_get_ufs_http_error(self, mock_get):
        # arrange
        date = '01-01-2022'
        mock_get.side_effect = requests.exceptions.HTTPError('Error')

        # act/assert
        with self.assertRaises(PageError):
            self.repo.get_ufs(date)
