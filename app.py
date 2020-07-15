from flask import Flask

app = Flask(__name__)

# Set up route
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)