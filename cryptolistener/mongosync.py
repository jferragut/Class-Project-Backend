from mongoengine import *
import time
import datetime

# Standard model that defines all Coin Data
class Asset(Document):
    name = StringField(max_length=50)
    symbol = StringField(max_length=7)
    rank = IntField(max_length=5)
    price_usd = DecimalField(max_value=None,precision=2)
    volume_24h_usd = DecimalField(max_value=None,precision=2)
    market_cap_usd = DecimalField(max_value=None,precision=2)
    available_supply = DecimalField(max_value=None,precision=2)
    total_supply = DecimalField(max_value=None,precision=2)
    percent_change_1h = DecimalField(min_value=None,max_value=None,precision=2)
    percent_change_24h = DecimalField(min_value=None,max_value=None,precision=2)
    percent_change_7d = DecimalField(min_value=None,max_value=None,precision=2)
    last_updated = DateTimeField(default=datetime.datetime.now)
    
    
class SyncDB(object):
    @classmethod
    def AddValues(cls, result, client, collection):
        for coin in result:
            theCoin = Asset.objects(name=coin['name']).first()
            if theCoin is None:
                theCoin = Asset()
            theCoin.symbol = coin['symbol']
            theCoin.rank = coin['rank']
            theCoin.price_usd = coin['price_usd']
            theCoin.volume_24h_usd = coin['24h_volume_usd']
            theCoin.market_cap_usd = coin['market_cap_usd']
            theCoin.total_supply = coin['max_supply']
            theCoin.percent_change_1h = coin['percent_change_1h']
            theCoin.percent_change_24h = coin['percent_change_24h']
            theCoin.percent_change_7d = coin['percent_change_7d']
            theCoin.save()
            theCount = Asset.objects.count()  
        epoctime = time.time()        
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoctime))
        print(str(timestamp)+": "+str(theCount)+" assets updated.")