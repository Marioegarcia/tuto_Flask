from wtforms import Form
from wtforms import validators
from wtforms import StringField,PasswordField,BooleanField
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
    username = StringField('', [
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])
    password = PasswordField('', [
        validators.Required(message='El password es requerido.'),
        
    ])


class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50),
        
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido.'),
        validators.Email(message='Ingre un email valido.')
    ])
    password = PasswordField('Password', [
        validators.Required('El password es requerido.'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide.')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('', [
        validators.DataRequired()
    ])
    
    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso.')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya se encuentra en uso.')                   