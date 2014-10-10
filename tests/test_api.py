import unittest
from blockr.api import Api
from blockr.service import ApiService

class TestApi(unittest.TestCase):
    """ Tests for the main Api class """

    def root_url(self, func, expected):
        """ Testing the root URI generation """
        self.assertEqual(func, expected)

    def setUp(self):
        """
        Setting up a few diffrent currencies. Basically they all follow the
        same "path" so they are not all in need for tests. Will add three
        for now.
        """
        self.ltc = ApiService('Litecoin')
        self.btc = ApiService('Bitcoin')
        self.dgc = ApiService('Digitalcoin')

        # One instance of the "real" APi class the user instantiates.
        # Because all methods are identical only need for one test instance.
        self.api = Api('Bitcoin')

    def test_bitcoin_base_url_builder(self):
        """ Testing bitcoin root URI """
        self.root_url(self.btc.build_url(), 'http://blockr.io/api/v1/')

    def test_litecoin_base_url_builder(self):
        """ Testing litecoin root URI """
        self.root_url(self.ltc.build_url(), 'http://ltc.blockr.io/api/v1/')

    def test_digitalcoin_base_url_builder(self):
        """ Testing digitalcoin root URI """
        self.root_url(self.dgc.build_url(), 'http://dgc.blockr.io/api/v1/')

    def test_coin_info(self):
        """ Testing the coin info HTTP call """

    def test_address_balance(self):
        self.assertEqual(self.api.address_balance(
            ["1PnhYci3BxgbnH3nDNwyb3uQvKxCgvkXy", "1PTDNVxrVwpwP6xUXqxB3uGTGmKJJ15U3f" ]),
            json.load('fixtures/address_balance.json')
        )


if __name__ == '__main__':
    unittest.main()
