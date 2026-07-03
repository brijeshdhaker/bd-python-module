from core_module.utils.Logger import Logger
from dbx_module.utils.SparkSessionManager import SparkSessionManager


class SparkReadHandler:
    
    #
    def __init__(self):
        self.spark = SparkSessionManager(self.__class__.__name__).create_session()
        self.logger = Logger(self.__class__.__name__)

    #
    def read_parquet(self, path):
        df = self.spark.read.parquet(path)
        return df
    
    #
    def read_json(self, path):
        import json
        with open(path) as f:
            config = json.load(f)
        return config