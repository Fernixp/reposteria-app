class Config:
    SECRET_KEY = "UNA_CONTRASEÑA_SEGURA"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@localhost:3307/reposteria"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    