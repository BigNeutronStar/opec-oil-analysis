import configparser

class Config:
    def __init__(self, config):
        self.report_dir = config['directories']['report_dir']
        self.personal_dir = config['directories']['personal_dir']

        self.databases = config['databases'] 
        self.personal_databases = config['personal_databases']
        self.graphics = config['graphics']

def Load():
    config = configparser.ConfigParser()
    config.read('Scripts/config.ini')

    return Config(config)