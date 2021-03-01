# imports
from flask import Flask, render_template, request
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
    target = request.args.get("target")
    if target == "ochratoxin":
        protein = ""
    if target == "vomitoxin":
        protein = ""
    if target == "tnf":
        protein = "MSTESMIRDVELAEEALPKKTGGPQGSRRCLFLSLFSFLIVAGATTLFCLLHFGVIGPQREEFPRDLSLISPLAQAVRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLDFAESGQVYFGIIAL"
    if target == "interferon":
        protein = "MALSFSLLMAVLVLSYKSICSLGCDLPQTHSLGNRRALILLAQMGRISHFSCLKDRHDFGFPEEEFDGHQFQKAQAISVLHEMIQQTFNLFSTEDSSAAWEQSLLEKFSTELYQQLNDLEACVIQEVGVEETPLMNEDSILAVRKYFQRITLYLTEKKYSPCAWEVVRAEIMRSLSFSTNLQKRLRRKD"
    if target == "interleukin": 
        protein = "MAEVPELASEMMAYYSGNEDDLFFEADGPKQMKCSFQDLDLCPLDGGIQLRISDHHYSKGFRQAASVVVAMDKLRKMLVPCPQTFQENDLSTFFPFIFEEEPIFFDTWDNEAYVHDAPVRSLNCTLRDSQQKSLVMSGPYELKALHLQGQDMEQQVVFSMSFVQGEESNDKIPVALGLKEKNLYLSCVLKDDKPTLQLESVDPKNYPKKKMEKRFVFNKIEINNKLEFESAQFPNWYISTSQAENMPVFLGGTKGGQDITDFTMQFVSS"       
    if target == "ptk":
        protein = "AIVFIKQPSSQDALQGRRALLRCEVEAPGPVHVYWLLDGAPVQDTERRFAQGSSLSFAAVDRLQDSGTFQCVARDDVTGEEARSANASFNIKWIEAGPVVLKHPASEAEIQPQTQVTLRCHIDGHPRPTYQWFRDGTPLSDGQSNHTVSSKERNLTLRPAGPEHSGLYSCCAHSAFGQACSSQNFTLSIADESFARVVLAPQDVVVARYEEAMFHCQFSAQPPPSLQWLFEDETPITNRSRPPHLRRATVFANGSLLLTQVRPRNAGIYRCIGQGQRGPPIILEATLHLAEIEDMPLFEPRVFTAGSEERVTCLPPKGLPEPSVWWEHAGVRLPTHGRVYQKGHELVLANIAESDAGVYTCHAANLAGQRRQDVNITVATVPSWLKKPQDSQLEEGKPGYLDCLTQATPKPTVVWYRNQMLISEDSRFEVFKNGTLRINSVEVYDGTWYRCMSSTPAGSIEAQARVQVLEKLKFTPPPQPQQCMEFDKEATVPCSATGREKPTIKWERADGSSLPEWVTDNAGTLHFARVTRDDAGNYTCIASNGPQGQIRAHVQLTVAVFITFKVEPERTTVYQGHTALLQCEAQGDPKPLIQWKGKDRILDPTKLGPRMHIFQNGSLVIHDVAPEDSGRYTCIAGNSCNIKHTEAPLYVVDKPVPEESEGPGSPPPYKMIQT"
    if target == "csn":
        protein = "MVKLAKAGKNQGDPKKMAPPPKEVEEDSEDEEMSEDEEDDSSGEEVVIPQKKGKKAAATSAKKVVVSPTKKVAVATPAKKAAVTPGKKAAATPAKKTVTPAKAVTTPGKKGATPGKALVATPGKKGAAIPAKGAKNGKNAKKEDSDEEEDDDSEEDEEDDEDEDEDEDEIEPAAMKAAAAAPASEDEDDEDDEDDEDDDDDEEDDSEEEAMETTPAKGKKAAKVVPVKAKNVAEDEDEEEDDEDEDDDDDEDDEDDDDEDDEEEEEEEEEEPVKEAPGKRKKEMAKQKAAPEAKKQKVEGTEPTTAFNLFVGNLNFNKSAPELKTGISDVFAKNDLAVVDVRIGMTRKFGYVDFESAEDLEKALELTGLKVFGNEIKLEKPKGKDSKKERDARTLLAKNLPYKVTQDELKEVFEDAAEIRLVSKDGKSKGIAYIEFKTEADAEKTFEEKQGTEIDGRSISLYYTGEKGQNQDYRGGKNSTWSGESKTLVLSNLSYSATEETLQEVFEKATFIKVPQNQNGKSKGYAFIEFASFEDAKEALNSCNKREIEGRAIRLELQGPRGSPNARSQPSKTLFVKGLSEDTTEETLKESFDGSVRARIVTDRETGSSKGFGFVDFNSEEDAKAAKEAMEDGEIDGNKVTLDWAKPKGEGGFGGRGGGRGGFGGRGGGRGGRGGFGGRGRGGFGGRGGFRGGRGGGGDHKPQGKKTKFE"
    if target == "vegf":
        protein = "MNFLLSWVHWSLALLLYLHHAKWSQAAPMAEGGGQNHHEVVKFMDVYQRSYCHPIETLVDIFQEYPDEIEYIFKPSCVPLMRCGGCCNDEGLECVPTEESNITMQIMRIKPHQGQHIGEMSFLQHNKCECRPKKDRARQEKKSVRGKGKGQKRKRKKSRYKSWSVYVGARCCLMPWSLPGPHPCGPCSERRKHLFVQDPQTCKCSCKNTDSRCKARQLELNERTCRCDKPRR"
    if target == "hiv": 
        protein = "FLDGIDKAQEEHEKYHSNWRAMASDFNLPPVVAKEIVASCDKCQLKGEAMHGQVDCSPGIWQLDCTHLEGKVILVAVHVASGYIEAEVIPAETGQETAYFLLKLAGRWPVKTVHTDNGSNFTSTTVKAACWWAGIKQEFGIPYNPQSQGVIESMNKELKKIIGQVRDQAEHLKTAVQMAVFIHNFKRKGGIGGYSAGERIVDIIATDIQTKELQKQITKIQNFRVYYRDSRDPVWKGPAKLLWKGEGAVVIQDNSDIKVVPRRKAKIIRDYGKQMAGDDCVASRQDED"         
    if target == "janus":
        protein = "MQYLNIKEDCNAMAFCAKMRSSKKTEVNLEAPEPGVEVIFYLSDREPLRLGSGEYTAEELCIRAAQACRISPLCHNLFALYDENTKLWYAPNRTITVDDKMSLRLHYRMRFYFTNWHGTNDNEQSVWRHSPKKQKNGYEKKKIPDATPLLDASSLEYLFAQGQYDLVKCLAPIRDPKTEQDGHDIENECLGMAVLAISHYAMMKKMQLPELPKDISYKRYIPETLNKSIRQRNLLTRMRINNVFKDFLKEFNNKTICDSSVSTHDLKVKYLATLETLTKHYGAEIFETSMLLISSENEMNWFHSNDGGNVLYYEVMVTGNLGIQWRHKPNVVSVEKEKNKLKRKKLENKHKKDEEKNKIREEWNNFSYFPEITHIVIKESVVSINKQDNKKMELKLSSHEEALSFVSLVDGYFRLTADAHHYLCTDVAPPLIVHNIQNGCHGPICTEYAINKLRQEGSEEGMYVLRWSCTDFDNILMTVTCFEKSEQVQGAQKQFKNFQIEVQKGRYSLHGSDRSFPSLGDLMSHLKKQILRTDNISFMLKRCCQPKPREISNLLVATKKAQEWQPVYPMSQLSFDRILKKDLVQGEHLGRGTRTHIYSGTLMDYKDDEGTSEEKKIKVILKVLDPSHRDISLAFFEAASMMRQVSHKHIVYLYGVCVRDVENIMVEEFVEGGPLDLFMHRKSDVLTTPWKFKVAKQLASALSYLEDKDLVHGNVCTKNLLLAREGIDSECGPFIKLSDPGIPITVLSRQECIERIPWIAPECVEDSKNLSVAADKWSFGTTLWEICYNGEIPLKDKTLIEKERFYESRCRPVTPSCKELADLMTRCMNYDPNQRPFFRAIMRDINKLEEQNPDIVSEKKPATEVDPTHFEKRFLKRIRDLGEGHFGKVELCRYDPEGDNTGEQVAVKSLKPESGGNHIADLKKEIEILRNLYHENIVKYKGICTEDGGNGIKLIMEFLPSGSLKEYLPKNKNKINLKQQLKYAVQICKGMDYLGSRQYVHRDLAARNVLVESEHQVKIGDFGLTKAIETDKEYYTVKDDRDSPVFWYAPECLMQSKFYIASDVWSFGVTLHELLTYCDSDSSPMALFLKMIGPTHGQMTVTRLVNTLKEGKRLPCPPNCPDEVYQLMRKCWEFQPSNRTSFQNLIEGFEALLK"
    XNAList = ["ANA", "CeNA", "FANA", "GNA", "LNA", "PNA", "TNA"]
    BaseList = ["G", "C", "A", "U"]
    sequence = ""
    for i in range(1):
        base = randint(0,3)
        sequence += BaseList[base]
    sequenceList = [sequence]
    affinities = {
        XNAList[0] : 0,
        XNAList[1] : 0,
        XNAList[2] : 0,
        XNAList[3] : 0,
        XNAList[4] : 0,
        XNAList[5] : 0,
        XNAList[6] : 0
    }
    for xna in XNAList:
        theList = sendStringsToTest(sequenceList, xna, protein)
        affinities[xna] = getTopN(1, 0, theList)
    return render_template('ModelFound.html', ANAaff=affinities["ANA"], CeNAaff= affinities["CeNA"], FANAaff=affinities["FANA"],
    GNAaff=affinities["GNA"], LNAaff=affinities["LNA"], PNAaff=affinities["PNA"], TNAaff=affinities["TNA"])

def predict_binding_api(smile, protien):
    url= 'https://modelforest.ai/predict/BindingPrediction/'
    data = json.dumps({
        'smiles':[smile],
        'target':protien,
        'token': 'B*drgZ4r<gxQV4C^Mv{RmJa{RHm$ukfEsaD' # This is a limited access API Key
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
    print(returnString)
    toReturn = float(returnString)
    return toReturn

def sendStringsToTest(sequenceList, XNA, protein):
    #returns a zipped list containing both binding affinities and base sequences
    bindingAffinities = []
    for sequence in sequenceList:
        smilesCode = ConvertStringToSMILES(sequence, XNA)
        responseText = predict_binding_api(smilesCode, protein)
        bindingAffinities.append(getBindingAffinity(responseText))
    affinity_string = zip(bindingAffinities, sequenceList)
    affinity_string = sorted(affinity_string, key = lambda z: z[0])
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
            i+=1
    else:
        while i < numberOfItems:
            toReturn.append(sequence[i])
            i+=1
    return toReturn

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
