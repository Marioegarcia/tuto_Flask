import datetime
#El .(punto) es para referencia que estamos
#importando desde nuestro modulo

#from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from . import db

class User(db.Model):
    __tablename__ = 'users'
    id         = db.Column(db.Integer, primary_key = True)
    username   = db.Column(db.String(50), unique=True, nullable=False )
    encrypted_password   = db.Column(db.String(93), nullable=False)
    email      = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    
    
    @property
    def password(self):
        pass
    
    
    @password.setter
    def password(self, value):
        self.encrypted_password = generate_password_hash(value)

    
    #sobrescribimos el metodo str(opcional) retornamios el user name
    #cada vez que se realice una impresion de tipo username se visualizara el username
    def __str__(self):
        return self.username

    @classmethod
    def create_element(cls, username, password, email):
        user = User(username= form.username, password=form.password, email=form.email)

        db.session.add(user)
        db.session.commit()

        return user

    # @classmethod
    # def get_by_username(cls, username):
    #     return User.query.filter_by(username=username).first()

    # @classmethod
    # def get_by_email(cls, email):
    #     return User.query.filter_by(email=email).first()
    