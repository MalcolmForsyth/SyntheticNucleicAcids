# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/XNAInfo')
def XNAInfo():
    return render_template('XNAInfo.html')

@app.route('/TargetInfo')
def TargetInfo():
    return render_template('TargetInfo.html')

@app.route('/model')
def Model():
    return render_template('XNAfinder.html')

@app.route('/modelfound')
def Modelfound():
    return render_template('ModelFound.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
