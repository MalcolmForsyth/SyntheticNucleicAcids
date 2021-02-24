# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # route and render the index page

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # route and render the welcome page

@app.route('/about')
def about():
    return render_template('about.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
