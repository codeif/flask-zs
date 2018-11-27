class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@db/demo'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
