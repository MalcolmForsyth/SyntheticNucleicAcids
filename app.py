# import the Flask class from the flask module
from flask import Flask, render_template

from random import randint, choice
from decimal import Decimal
import json, requests

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

def predict_binding_api(smile, protien):
    url= 'https://modelforest.ai/predict/BindingPrediction/'
    data = json.dumps({
        'smiles':[smile],
        'target':protien,
        'token': 'IfZyHl3S9SiJvSkUcMr_EcKZ4Z6qBJiKB3oSShVN' # This is a limited access API Key
        })                                             # Go to https://modelforest.ai/pricing/ and register to get a full access API key
    headers = {'content-type': 'application/json'} 
    response = requests.post(url, headers=headers, data=data) 
    return response.text

def AlterNucleobaseString(sequence, mods_left):
    #Recursively modifies the base sequence. Set mods_left to ~3 when starting the modification
    if mods_left == 0:
        return sequence
    alter_mode = randint(1,3)
    if alter_mode == 1:
        #AddNucleobase
        if len(sequence) == 30:
            AlterNucleobaseString(sequence, mods_left)
        insertIndex = randint(0, len(sequence))
        insertBase = choice('ACGU')
        sequence = sequence[0:insertIndex] + insertBase + sequence[insertIndex:len(sequence)]      
    elif alter_mode == 2:
        #RemoveNucleobase
        if len(sequence) == 10:
            AlterNucleobaseString(sequence, mods_left)
        removeIndex = randint(0,len(sequence)-1)
        sequence = sequence[0:removeIndex] + sequence[removeIndex+1:len(sequence)]
    else:
        #ChangeNucleobase
        changeIndex = randint(0, len(sequence)-1)
        changeBase = choice('ACGU')
        sequence = sequence[0:changeIndex] + changeBase + sequence[changeIndex+1:len(sequence)]
    toReturn = AlterNucleobaseString(sequence, mods_left-1)
    return toReturn
   
def ConvertStringToSMILES(sequence, XNA_name):
    #Transforms a sequence of bases into a SMILES code the API can understand
    ASmiles = "N3C=NC4C(N)=NC=NC=4-3"
    GSmiles = "N3C=NC4C(=O)NC(N)=NC=4-3"
    CSmiles = "N3C(=O)N=C(N)C=C3"
    USmiles = "N3C(=O)NC(=O)C=C3"
    toReturn = ""
    if XNA_name == "CeNA":
        
        for letter in sequence:
            if letter == "A":
                toReturn += "C1C(C=CC(" + ASmiles + ")C1)COP([S-])(=O)O"
            elif letter == "G":
                toReturn += "C1C(C=CC(" + GSmiles +")C1)COP([S-])(=O)O"
            elif letter == "U":
                toReturn  += "C1C(C=CC(" + USmiles +")C1)COP([S-])(=O)O"
            elif letter == "C":
                toReturn  += "C1C(C=CC("+CSmiles+")C1)COP([S-])(=O)O"
    elif XNA_name == "GNA":
        
        for letter in sequence:
            if letter == "A":
                toReturn += "C1(C("+ASmiles+"))COP([S-])(=O)O"
            elif letter == "G":
                toReturn += "C1(C("+GSmiles+"))COP([S-])(=O)O"
            elif letter == "U":
                toReturn += "C1(C("+USmiles+"))COP([S-])(=O)O"
            elif letter == "C":
                toReturn += "C1(C("+CSmiles+"))COP([S-])(=O)O"
    elif XNA_name == "TNA":
        
        for letter in sequence:
            if letter == "A":
                
                toReturn += "C1C(OC1("+ASmiles+")COP(=O)([S-])O"
            elif letter == "G":
                
                toReturn += "C1C(OC1("+GSmiles+")COP(=O)([S-])O"
            elif letter == "U":
                
                toReturn += "C1C(OC1("+USmiles+")COP(=O)([S-])O"
            elif letter == "C":
                
                toReturn += "C1C(OC1("+CSmiles+")COP(=O)([S-])O"
    elif XNA_name == "ANA":
        
        for letter in sequence:
            if letter == "A":
                
                toReturn += "C1OC("+ASmiles+")C(O)C1OP([S-])(=O)O"
            elif letter == "G":
                
                toReturn += "C1OC("+GSmiles+")C(O)C1OP([S-])(=O)O"
            elif letter == "U":
                
                toReturn += "C1OC("+USmiles+")C(O)C1OP([S-])(=O)O"
            elif letter == "C":
                
                toReturn += "C1OC("+CSmiles+")C(O)C1OP([S-])(=O)O"
    elif XNA_name == "FANA":
        
        for letter in sequence:
            if letter == "A":
                toReturn += "C1OC("+ASmiles+")C(F)C1OP([S-])(=O)O"
            elif letter == "G":
                toReturn += "C1OC("+GSmiles+")C(F)C1OP([S-])(=O)O"
            elif letter == "U":
                toReturn += "C1OC("+USmiles+")C(F)C1OP([S-])(=O)O"
            elif letter == "C":
                toReturn += "C1OC("+CSmiles+")C(F)C1OP([S-])(=O)O"
    elif XNA_name == "PNA":
        
        for letter in sequence:
            if letter == "A":
                toReturn += "CNC(=O)CN(C(=O)C"+ASmiles+")C"
            elif letter == "G":
                toReturn += "CNC(=O)CN(C(=O)C"+GSmiles+")C"
            elif letter == "U":
                toReturn += "CNC(=O)CN(C(=O)C"+USmiles+")C"
            elif letter == "C":
                toReturn += "CNC(=O)CN(C(=O)C"+CSmiles+")C"
    else:
         #(LNA)
        for letter in sequence:
            if letter == "A":
                
                toReturn += "C1C2(COC1C("+ASmiles+")O2)COP(=O)([S-])O"
            elif letter == "G":
                
                toReturn += "C1C2(COC1C("+GSmiles+")O2)COP(=O)([S-])O"
            elif letter == "U":
                
                toReturn += "C1C2(COC1C("+USmiles+")O2)COP(=O)([S-])O"
            elif letter == "C":
                
                toReturn += "C1C2(COC1C("+CSmiles+")O2)COP(=O)([S-])O"
    return toReturn

def getBindingAffinity(responseText):
    #Trims the API's response text to just the binding affinity
    startIndex = responseText.rfind('[')
    lastIndex = responseText.find(']', startIndex)
    returnString = responseText[startIndex+1:lastIndex]
    toReturn = Decimal(returnString)
    return toReturn

def sendStringsToTest(sequenceList, XNA, protein):
    #returns a zipped list containing both binding affinities and base sequences
    bindingAffinities = []
    for sequence in sequenceList:
        smilesCode = convertStringToSMILES(sequence, XNA)
        responseText = predict_binding_api(smilesCode, protein)
        bindingAffinities.append(getBindingAffinity(responseText))
    affinity_string = zip(bindingAffinities, sequenceList)
    affinity_string = affinity_string.sort()
    return affinity_string

def getTopN(numberOfItems, fromWhichList, theList):
    #Gets the first N elements from a specific list in a zipped list
    #0 is for affinities, 1 is for sequence string
    affinity, sequence = zip(*theList)
    toReturn = []
    i = 0
    if fromWhichList == 0:
        while i < numberOfItems:
            toReturn.append(affinity[i])
            i++
    else:
        while i < numberOfItems:
            toReturn.append(sequence[i])
            i++
    return toReturn

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
