# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('aboutEOH.html')

@app.route('/XNAInfo')
def XNAInfo():
    return render_template('XNAInfo.html')

@app.route('/TargetInfo')
def XNAInfo():
    return render_template('TargetInfo.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
