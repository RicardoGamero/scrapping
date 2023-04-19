from unittest import TestCase
from unittest.mock import MagicMock
from app.models.uf import UF
from app.repositories.uf_repository import UfRepository
from app.services.uf_service import UfService


class TestUfService(TestCase):
    def setUp(self):
        self.mock_uf_repository = MagicMock(spec=UfRepository)
        self.uf_service = UfService(self.mock_uf_repository)

    def test_get_ufs(self):
        date = "2022-04-18"
        expected_ufs = [UF(date=date, value=100), UF(date=date, value=200)]
        self.mock_uf_repository.get_ufs.return_value = expected_ufs

        result = self.uf_service.get_ufs(date)

        self.assertEqual(result, expected_ufs)
        self.mock_uf_repository.get_ufs.assert_called_once_with(date)
