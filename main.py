from flask import Flask, request, render_template, send_from_directory
import random

global meetings
meetings = {}

global call, ans, ice
call, ans, ice = None, None, None

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Share')
def sender():
    return render_template('Share.html')


@app.route('/Receive')
def receiver():
    return render_template('Receive.html')


@app.route('/Closed')
def closed():
    return render_template('Closed.html')


@app.route('/Help')
def help():
    return render_template('Help.html')


@app.route('/assets/<path:path>')
def send_report(path):
    return send_from_directory('assets', path)


#Using Bulma 0.7.2 and Jquery 1.10.2


@app.route('/getId')
def getId():
    global meetings
    SDP = request.args.get("sdp")
    #ICE = request.args.get("ice")
    assert SDP != ''
    #assert ICE != ''
    while True:
        MeetingId = str(random.randint(100, 999))
        try:
            meetings[MeetingId]
            continue
        except KeyError:
            break
    meetings[MeetingId] = {'sdp': SDP, 'ice': '', 'ans': None}
    print("New meeting: " + MeetingId)
    print(SDP)
    #print(ICE)
    return MeetingId


@app.route('/connectId')
def connectId():
    global meetings
    MeetingId = request.args.get("id")
    try:
        return meetings[MeetingId]['sdp']
    except KeyError:
        return "None"


@app.route('/sendAns')
def sendAns():
    global meetings
    MeetingId = request.args.get('id')
    ICE = request.args.get('ice')
    Ans = request.args.get('ans')
    assert Ans != ''
    assert ICE != ''
    assert MeetingId != ''
    meetings[MeetingId]['ans'] = Ans
    meetings[MeetingId]['ice'] += ICE + "\n"
    return "Sent"


@app.route('/checkAns')
def checkAns():
    global meetings
    MeetingId = request.args.get("id")
    print(MeetingId)
    try:
        if meetings[MeetingId]['ans'] == None:
            return "wait"
        else:
            return meetings[MeetingId]['ans']
    except KeyError:
        return "wait"


@app.route('/getIce')
def getIce():
    global meetings
    MeetingId = request.args.get("id")
    if meetings[MeetingId]['ice'] == '':
        return "wait"
    else:
        return meetings[MeetingId]['ice']


app.run(host='0.0.0.0', port=81)

#Old code when I was trying out stuff
'''@app.route('/ICUCast')
def senderICU():
    return render_template('Share2.html')
@app.route('/S')
def sender2():
    return render_template('S.html')


@app.route('/R')
def receiver2():
    return render_template('R.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/getName')
def whoami():
    return "3 Charity Integrated Classroom Unit"


@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')


@app.route('/connect')
def connect():
    global call
    if request.args.get('sdp') != None:
        call = request.args.get('sdp')
        return "sent"
    else:
        return "missing ans"


@app.route('/getAns')
def getAns():
    global ans
    if ans != None:
        return ans
    else:
        return "no ans"


@app.route('/getIce2')
def getIce2():
    global ice
    if ice != None:
        return ice
    else:
        return "no ice"


@app.route('/getCall')
def getCall():
    global call
    if call != None:
        return call
    else:
        return "no call"


@app.route('/sendAns2')
def sendAns2():
    if True:
        global ans, ice
        if request.args.get('ans') == None:
            return "missing ans"
        elif request.args.get('ice') == None:
            return "missing ice"
        else:
            ice = request.args.get('ice')
            ans = request.args.get('ans')
            return "wait for client"
    else:
        return "You are not authorised to visit this page."


@app.route('/clearConn')
def clearConnections():
    if True:
        global call, ans, ice
        call, ans, ice = None, None, None
        return "Done"
    else:
        return "You are not authorised to visit this page."


@app.route('/ICUClosed')
def ICUClosed():
    return render_template("Closed2.html")'''
