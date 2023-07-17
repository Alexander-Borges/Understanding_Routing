from flask import Flask 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<text>')
def say(text):
    print(text)
    return "Say " + text.capitalize() + "!"

@app.route('/repeat/<int:num>/<text>')
def repeat(num, text):
    print(num)
    print(text)
    return f"{text * num}"

# Default route for any other url
@app.route('/', defaults ={'path': ''})
@app.route('/<path:path>')
def default_route(path):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)