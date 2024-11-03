import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///users.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
