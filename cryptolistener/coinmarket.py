from coinmarketcap import Market


class CoinMarketWrapper:
    def Get_Currencies(self):
        coinmarketcap = Market()
        a = coinmarketcap.ticker(start=0, limit=100, convert="USD")
        # print(a)
        return a