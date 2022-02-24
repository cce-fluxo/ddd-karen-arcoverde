from os import environ

#Configuracoes gerais, o SQLALCHEMY_DATABASE_URI  é trocado ao reiniciar o banco de dados
class Config:

    # DATABASE - configuracao da database (modo web-dev)
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application - configuracao da comunicacao com o front-end
    SECRET_KEY = environ.get('SECRET_KEY')
    JSON_SORT_KEYS = False
    DEBUG = True

    ## MAIL ## 
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_USE_TLS = True
    MAIL_USE_SSH = False
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')

    ### JWT EXTENDED ##
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')

    