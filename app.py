from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] 

@app.route("/")
def pagina_inicial():
    return "Hello World, Testando o Projeto"

if __name__ == '__main__':
    app.run()
