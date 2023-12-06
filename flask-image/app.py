from flask import Flask
app = Flask(__name__)

@app.route('/')
def Content():
    return '<h1>Hello from MiniKube Pods</h2>'

if __name__ == "__main__":
    app.run()