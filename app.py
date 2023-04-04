from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

@app.route('/bug')                                                                                                                                
def bad():                                                                                                                                        
    try:                                                                                                                                          
        raise TypeError()                                                                                                                         
    except TypeError as e:                                                                                                                        
        print(e)                                                                                                                                  
    except TypeError as e:                                                                                                                        
        print("Duplicado, ou seja, nunca vai entrar aqui.")    


if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)