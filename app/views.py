# Se importan Clases
from flask import Blueprint
#Se importan Funciones
from flask import render_template,request, flash

from .forms import LoginForm , RegisterForm
from .models import User

page = Blueprint('page', __name__)

@page.app_errorhandler(404)         
def page_not_found(error):
    return render_template('errors/404.html'), 404

#index
@page.route('/')
def index():
   
    return render_template('index.html', title='Home')

#login
@page.route('/login', methods=['GET', 'POST'])
def login():
   
   form = LoginForm(request.form)
  
   
   if request.method == 'POST' and form.validate():
      print(form.username.data)
      print(form.password.data)
      print("Datos")
      flash('Bienvenido ' + form.username.data)
      
   return render_template('auth/login.html', title='login', form=form)

#Register
@page.route('/register', methods=['GET', 'POST'])
def register():
   
   form = RegisterForm(request.form)
   
   if request.method == 'POST':
      if form.validate():
         user = User.create_element(form.username.data, form.password.data, form.email.data)
         flash("USER_CREATED")
         print("usuario creado de forma exitosa")
         print(user.id)
   
         
         
         
   return render_template('auth/register.html', title='Registro',
                          form=form)
   
   


#About
@page.route('/about')
def about():
   
   return render_template('about.html', title='About')

