class Config:
    SECRET_KEY = 'codigofacilito'

class DevelopmentConfig(Config):
    pass_db  = 'mysql+pymysql://root:marioegh92@'
    base_dir = '127.0.0.1'
    dbname   =  '/web_flask'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = pass_db + base_dir + dbname
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:contraseña@direccion/nombre_db'
    #'mysql+pymysql://root:@localhost/project_web_facilito'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    
}