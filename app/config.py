from os import environ

#Configuracoes gerais, o SQLALCHEMY_DATABASE_URI  é trocado ao reiniciar o banco de dados
class Config:

    # DATABASE - configuracao da database (modo web-dev)
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = 'postgresql://bsbgwxvwvafuja:4d6c8157443b0e75b6c63579ce1af07b2eddd8d913bcac042c2ab5f0ca28b374@ec2-54-83-21-198.compute-1.amazonaws.com:5432/dcb8u6m5sti6dt'
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

    