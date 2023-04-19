import unittest
from app.models.uf import UF


class UFTestCase(unittest.TestCase):

    def setUp(self):
        self.uf = UF('18-04-2022', 30000.0)

    def test_to_dict(self):
        uf_dict = self.uf.to_dict()
        self.assertEqual(uf_dict['date'], '18-04-2022')
        self.assertEqual(uf_dict['value'], 30000.0)
