
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Петя Пидор!!!"
 
if __name__ == "__main__":
    app.run()
    
#Теперь нужно запустить, через python simple_flask.py