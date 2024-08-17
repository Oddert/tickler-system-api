from configparser import ConfigParser

config = ConfigParser()

config.read('./envfile.ini', encoding='utf8')

for section in config.sections():
    print(section)
    for key, value in config.items(section):
        print(key, value)
        globals()[key] = value.lower()
