import configparser


class Config:
    def __init__(self):
        self.configParser = configparser.RawConfigParser()
        self.configFilePath = r'config.ini'
        self.configParser.read(self.configFilePath)