from configparser import ConfigParser

config = ConfigParser()

config.read('./envfile.ini', encoding='utf8')

for section in config.sections():
    print(section)
    for key, value in config.items(section):
        print(key, value)
        globals()[key] = value.lower()

DATABASE_URI = 'sqlite:///./local-database.db'
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
JWT_ALGORITHM = 'HS256'
# JWT_SECRET_KEY = globals()['JWT_SECRET_KEY']
# JWT_REFRESH_SECRET_KEY = globals()['JWT_REFRESH_SECRET_KEY']
JWT_SECRET_KEY = config['DEFAULT']['JWT_SECRET_KEY']
JWT_REFRESH_SECRET_KEY = config['DEFAULT']['JWT_REFRESH_SECRET_KEY']
