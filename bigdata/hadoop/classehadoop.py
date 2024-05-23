
import time
import zookeeper
from hadoop import Hadoop
from hbase import HBase
from hive import Hive
from ignite import Ignite
class ConfigEngine(object):
    def __init__(self):
        self.zookeeper = Zookeeper()
        self.hadoop = Hadoop()
        self.hbase = HBase()
        self.hive = Hive()
        self.ignite = Ignite()
        
    def waiting(self):
        while True:
            print('Waiting...')
            time.sleep(5)
    
    def configure(self):
        self.zookeeper.configure()
        self.hadoop.configure()
#         self.hbase.configure()
        self.hive.configure()
        self.ignite.configure()
        
if __name__ == '__main__':
    configEngine = ConfigEngine()
    configEngine.configure()
    configEngine.waiting()