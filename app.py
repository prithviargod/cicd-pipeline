from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello CICD World!"

if __name__ == "__main__":
   app.hello();
