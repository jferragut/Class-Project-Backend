import time
from mongoengine import *
import pymongo
from pymongo import MongoClient
from cryptolistener.coinmarket import CoinMarketWrapper
from cryptolistener.mongosync import SyncDB

if __name__ == "__main__":
    starttime = time.time()
    client = connect('cryptolistener')
    collection = client.asset
    while True:
        coins = CoinMarketWrapper()
        result = coins.Get_Currencies()
        SyncDB.AddValues(result, client, collection)
        time.sleep(10.0 - ((time.time() - starttime) % 10.0))