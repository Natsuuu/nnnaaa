# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from gtts import gTTS
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import time,random,sys,json,codecs,threading,glob,ast,codecs,os,pytz,re,random,requests,time,urllib.parse
listApp = ["CHROMEOS", "DESKTOPWIN", "DESKTOPMAC", "IOSIPAD", "WIN10"]

client = LINE("ExwZTOuqdOdmMqP7owh0.IbugdJmH9mG2x9CA4fVIia.NmuBLe0p1BcIiudORvgS408TdUBC0dgRYenMe4CACW0=")
client.log("Auth Token : " + str(client.authToken))
KB = LINE("ExcT6iQ9NodUJO5QJ3R2.untHL8qTBS4KXZII1WIyeG.QSzGfUmVEIrpmpnDGN0IRKqAX3fMicklZ9GHLkhqYcA=")
client.log("Auth Token : " + str(KB.authToken))
KC = LINE("Ex6jezGFt2UroOMlJJ15.7R/mj1CHAYNrTygiXRE8Lq.vd95juTTvy6YikXY58jPhze6b+Pzg9yk04U9rTEVm/8=")
client.log("Auth Token : " + str(KC.authToken))
KD = LINE("ExxBf63FDVX116oNFnrd.lrqUwX5AeToRMjnBOgWcNq.xRue3ERHSwjPva/6p1HBDdTNpVKCyMcP4AXATLM/G5E=")
client.log("Auth Token : " + str(KD.authToken))
KE = LINE("ExvlRv3ltDENmNqK90te.EAJRUKwTjYEm48/0KX0mxG.i8uLwIn8vZbW2XyJCGWpXTJfwb2X7V5StG0/41wB6hU=")
client.log("Auth Token : " + str(KE.authToken))
KF = LINE("Exa6aGzsuLvaoCkRPux3.PXxVoKegXtIiQ1v4WbUmiW.u08GeosyA9s1ik99QpCnTiF/+yMgbRGhc4Sef2TjVng=")
client.log("Auth Token : " + str(KF.authToken))
KG = LINE("ExHTSfn2MaYv0A6DQ1L0.K3+hRz0vYzqZRueEHTmW8a.tFuvyXKVcHQvMQqjprVidFaBIEQfb/MlVDf+fghbuGA=")
client.log("Auth Token : " + str(KG.authToken))
KH = LINE("Ex8PIYI5End1hVbobQu9.2Qz3M2q6TaqxIhzPAQaSMq.Vg5GB+bLjZwcUXYu7XxGM//J+/14DxstWBBqhK1WH4Y=")
client.log("Auth Token : " + str(KH.authToken))
KI = LINE("Exq6kVBDlTAw3tOn8tN6.iJduZ1MiG2pm4+veQogk1G.0C+/wpT+z8lZnShI62Hcr3MvEJs1jy1iK0uDn7fCSSc=")
client.log("Auth Token : " + str(KI.authToken))
KJ = LINE("ExvVWGoJD05iyoRFgTg1.aVTNWw9Djfsbv5gWo8Cl8q.7uh28GTfvxjpah6ycXogqR0QASCTLJ1YH0mTsVwqnuk=")
client.log("Auth Token : " + str(KJ.authToken))
#client.log("Auth Token : " + str(KJ.authToken))
#KK = LINE("EwcinY7GYbIeSMBxbNjd.qHhq/Cl/td+ZILtuK79Z+q.cGRBQK2g4I0oWrdG5Q7UJ9AjSWIZeLg+P3PeHnEgHlE=")
#client.log("Auth Token : " + str(KK.authToken))
#KL = LINE("EwGf4mM9YEQtCwM9uIQa.ELQkNHQtk6pJZe1XvZtiQG.qfIab0omaxsUpdzek/urOjSeZZRY8gWzt2pcYZz0RFk=")
#client.log("Auth Token : " + str(KL.authToken))
#KM = LINE("EwKjTGfhyAlmSJe5EZS9.vQMo/A1Ck97/oALSyJARcq.GyMSqwE+Xfd3bEsIs25B+Q/LqZ0wb9mFlPQKEWy2O+g=")
#client.log("Auth Token : " + str(KM.authToken))
#KN = LINE("EwQEhUpqvFuGslDwvNrb.6/QH7FvRpWk6w6QcOI3dYW.NGlaTCpfEo8zzC1nVKbvdCaq6FshyvopysxsGya2PlQ=")
#client.log("Auth Token : " + str(KN.authToken))
#KO = LINE("EwQEhUpqvFuGslDwvNrb.6/QH7FvRpWk6w6QcOI3dYW.NGlaTCpfEo8zzC1nVKbvdCaq6FshyvopysxsGya2PlQ=")
#client.log("Auth Token : " + str(KN.authToken))
#KP = LINE("EwfcGahc1tYnrgXRptjb.7WDvCUCOHuMK/nUvAnmjIW.PG0uQxu9ghAjSJ5bB1CZ8DVQdmfoIBwZTs/fLT22bK4=")
#client.log("Auth Token : " + str(KP.authToken))

clientPoll = OEPoll(client)


BOT=[client,KB,KC,KD,KE,KF,KG,KH,KI,KJ]
KAC=[KB,KC,KD,KE,KF,KG,KH,KI,KJ]

profile, setting = client.getProfile(), client.getSettings()
pB,setting_B = KB.getProfile(),KB.getSettings()
pC,setting_C = KC.getProfile(),KC.getSettings()
pD,setting_D = KD.getProfile(),KD.getSettings()
pE = KE.getProfile()
pF = KF.getProfile();pG = KG.getProfile();pH = KH.getProfile();pI = KI.getProfile();pJ = KJ.getProfile()
#;pK = KK.getProfile();pL = KL.getProfile();pM = KM.getProfile();pN = KN.getProfile();pO = KO.getProfile()

offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

wait = {
    'bye':{},
    'readPoint':{},
    'rapidFire':{},
    'readMember':{},
    'protect':{},
    'PROTECTURLINVITECHANGE':{},
    'PROTECTKICK':{},
    'PROTECTGNAMECHANGE':{},
    'MessageCount':{},
    'setTime':{},
    'kick':{},
    'blacklist':{},
    'wblacklist':{},
    'wdblacklist':{},
    'ROM':{},
    "k1":"1",
    "k2":"2",
    "k3":"3",
    "k4":"4",
    "k5":"5",
    "k6":"6",
    "k7":"7",
    "k8":"8",
    "k9":"9",
    "k10":"10",
    "k11":"11",
    "k12":"12",
    "k13":"13",
    "k14":"14",
    "k15":"15",
    "clock":"16",
   }

f=codecs.open('black.json','r','utf-8')
wait["blacklist"] = json.load(f)

gname = {}
gname = wait["PROTECTGNAMECHANGE"]
setTime = {}
setTime = wait["setTime"]
#print type(wait)
res = {
    'num':{},
    'us':{},
    'au':{},
    }
#awr = LINE("Ew2r2RSnKvjaIJR5EYQ1.FB5KDVC+b6yYi34MxV05Cq.2lslgJMnSkZQj5gbg/oR76hzMlz2wuT1Gjk/6+ovPMs=")
#awq = LINE("EwOn4uyKr3p7BeaGX5l9.IqASYQ3G2Z01mSWXTr/IIq.Dfb6/pxJT0UAvGL7sboe9lpoQFw6ZHaLCtfn5JUCCPc=")
#awd = LINE("Ewz7Whz6p1s5fbLM8wh2.06pTVXWqTohUw/3tba0e8G.OIVU8ANN8ZhFBgCmiyjBHyywQNhHlwDdHcBi8YqIh68=")
#Aw = aws.getProfile()
#Ae = awe.getProfile()
#Ar = awr.getProfile()
#Aq = awq.getProfile()
#Ad = awd.getProfile()
admins=["ub8e7149e73a2ebf0d049b17e2c00a27a"]
#最高管理者
p1 = ["u16b9023f09732bdb0e4e36ddb437de11"]
#招待、保護、保護　オフ、kick、終了、保存、ブラック追加・削除が可能
p2 =[]
#招待、保護、保護　オフ、kick、が可能
p3 = []
#招待、保護、保護　オフ、が可能
haveP = admins + p1 + p2 + p3
ki = [pB.mid,pC.mid,pD.mid,pE.mid,pF.mid,pG.mid,pH.mid,pJ.mid]
bots = [profile.mid,pB.mid,pC.mid,pD.mid,pE.mid,pF.mid,pG.mid,pH.mid,pJ.mid]
#print wait


sendMessage = client.sendMessage
print (u'実行しました')
def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def cmi(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if texX + command in string:
                return True
    return False

def cmd(text, commands):
    for command in commands:
        if command in text:
            return True
    return False

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    """op.param1がgid
       op.param2が蹴った人
       op.param3が蹴られた人"""
    #print op
    try:
        if op.param2 in ki:
            return
        elif op.param3 in ki:
            try:
                bot = random.choice(KAC)
                G = bot.getGroup(op.param1)
                G.preventedJoinByTicket = False
                bot.updateGroup(G)
                Ticket = bot.reissueGroupTicket(op.param1)
            except:
                try:
                    bot = random.choice(KAC)
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(op.param1)
                except:
                    try:
                        bot = random.choice(KAC)
                        G = bot.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bot.updateGroup(G)
                        Ticket = bot.reissueGroupTicket(op.param1)
                    except:
                        try:
                            bot = random.choice(KAC)
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot.updateGroup(G)
                            Ticket = bot.reissueGroupTicket(op.param1)
                        except:
                            try:
                                bot = random.choice(KAC)
                                G = bot.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                bot.updateGroup(G)
                                Ticket = bot.reissueGroupTicket(op.param1)
                            except:
                                try:
                                    bot = random.choice(KAC)
                                    G = bot.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    bot.updateGroup(G)
                                    Ticket = bot.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        bot = random.choice(KAC)
                                        G = bot.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        bot.updateGroup(G)
                                        Ticket = bot.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            bot = random.choice(KAC)
                                            G = bot.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            bot.updateGroup(G)
                                            Ticket = bot.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                bot = random.choice(KAC)
                                                G = bot.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                bot.updateGroup(G)
                                                Ticket = bot.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    bot = random.choice(KAC)
                                                    G = bot.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    bot.updateGroup(G)
                                                    Ticket = bot.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        bot = random.choice(KAC)
                                                        G = bot.getGroup(op.param1)
                                                        G.preventedJoinByTicket = False
                                                        bot.updateGroup(G)
                                                        Ticket = bot.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            bot = random.choice(KAC)
                                                            G = bot.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            bot.updateGroup(G)
                                                            Ticket = bot.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                bot = random.choice(KAC)
                                                                G = bot.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                bot.updateGroup(G)
                                                                Ticket = bot.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    bot = random.choice(KAC)
                                                                    G = bot.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bot.updateGroup(G)
                                                                    Ticket = bot.reissueGroupTicket(op.param1)
                                                                except:
                                                                    try:
                                                                        bot = random.choice(KAC)
                                                                        G = bot.getGroup(op.param1)
                                                                        G.preventedJoinByTicket = False
                                                                        bot.updateGroup(G)
                                                                        Ticket = bot.reissueGroupTicket(op.param1)
                                                                    except:
                                                                        pass
            if op.param2 in haveP:
                for x in KAC:
                    x.acceptGroupInvitationByTicket(op.param1,Ticket)
            else:
                #if op.param3 == pB.mid:
                    #KB.acceptGroupInvitationByTicket(op.param1,Ticket)
                for x in KAC:
                    x.acceptGroupInvitationByTicket(op.param1,Ticket)
                try:
                    bot = random.choice(KAC)
                    bot.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        bot = random.choice(KAC)
                        bot.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                if op.param2 in wait["blacklist"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    f=codecs.open('blacklist.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            try:
                bot = random.choice(KAC)
                G = bot.getGroup(op.param1)
                G.preventedJoinByTicket = True
                bot.updateGroup(G)
            except:
                try:
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
                except:
                    try:
                        bot = random.choice(KAC)
                        G = bot.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bot.updateGroup(G)
                    except:
                        try:
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            bot.updateGroup(G)
                        except:
                            try:
                                bot = random.choice(KAC)
                                G = bot.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                bot.updateGroup(G)
                            except:
                                try:
                                    G = bot.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    bot.updateGroup(G)
                                except:
                                    try:
                                        bot = random.choice(KAC)
                                        G = bot.getGroup(op.param1)
                                        G.preventedJoinByTicket = True
                                        bot.updateGroup(G)
                                    except:
                                        try:
                                            G = bot.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            bot.updateGroup(G)
                                        except:
                                            try:
                                                bot = random.choice(KAC)
                                                G = bot.getGroup(op.param1)
                                                G.preventedJoinByTicket = True
                                                bot.updateGroup(G)
                                            except:
                                                try:
                                                    G = bot.getGroup(op.param1)
                                                    G.preventedJoinByTicket = True
                                                    bot.updateGroup(G)
                                                except:
                                                    try:
                                                        bot = random.choice(KAC)
                                                        G = bot.getGroup(op.param1)
                                                        G.preventedJoinByTicket = True
                                                        bot.updateGroup(G)
                                                    except:
                                                        try:
                                                            G = bot.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            bot.updateGroup(G)
                                                        except:
                                                            try:
                                                                bot = random.choice(KAC)
                                                                G = bot.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                bot.updateGroup(G)
                                                            except:
                                                                try:
                                                                    G = bot.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bot.updateGroup(G)
                                                                except:
                                                                    try:
                                                                        bot = random.choice(KAC)
                                                                        G = bot.getGroup(op.param1)
                                                                        G.preventedJoinByTicket = True
                                                                        bot.updateGroup(G)
                                                                    except:
                                                                        try:
                                                                            G = bot.getGroup(op.param1)
                                                                            G.preventedJoinByTicket = True
                                                                            bot.updateGroup(G)
                                                                        except:
                                                                            pass
        elif profile.mid == op.param3:
            #print "w"
            try:
                if op.param2 in haveP:
                    try:
                        bot = random.choice(KAC)
                        G = bot.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bot.updateGroup(G)
                        Ticket = bot.reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        bot.updateGroup(G)
                    except:
                        try:
                            bot = random.choice(KAC)
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot.updateGroup(G)
                            Ticket = bot.reissueGroupTicket(op.param1)
                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventedJoinByTicket = True
                            bot.updateGroup(G)
                        except:
                            try:
                                bot = random.choice(KAC)
                                G = bot.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                bot.updateGroup(G)
                                Ticket = bot.reissueGroupTicket(op.param1)
                                client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G.preventedJoinByTicket = True
                                bot.updateGroup(G)
                            except:
                                try:
                                    bot = random.choice(KAC)
                                    G = bot.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    bot.updateGroup(G)
                                    Ticket = bot.reissueGroupTicket(op.param1)
                                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G.preventedJoinByTicket = True
                                    bot.updateGroup(G)
                                except:
                                    try:
                                        bot = random.choice(KAC)
                                        G = bot.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        bot.updateGroup(G)
                                        Ticket = bot.reissueGroupTicket(op.param1)
                                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        bot.updateGroup(G)
                                    except:
                                        try:
                                            bot = random.choice(KAC)
                                            G = bot.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            bot.updateGroup(G)
                                            Ticket = bot.reissueGroupTicket(op.param1)
                                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            bot.updateGroup(G)
                                        except:
                                            try:
                                                bot = random.choice(KAC)
                                                G = bot.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                bot.updateGroup(G)
                                                Ticket = bot.reissueGroupTicket(op.param1)
                                                client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                G.preventedJoinByTicket = True
                                                bot.updateGroup(G)
                                            except:
                                                try:
                                                    bot = random.choice(KAC)
                                                    G = bot.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    bot.updateGroup(G)
                                                    Ticket = bot.reissueGroupTicket(op.param1)
                                                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    G.preventedJoinByTicket = True
                                                    bot.updateGroup(G)
                                                except:
                                                    pass
                else:
                    try:
                        bot = random.choice(KAC)
                        bot.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            bot = random.choice(KAC)
                            bot.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                bot = random.choice(KAC)
                                bot.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    bot = random.choice(KAC)
                                    bot.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                    try:
                        bot = random.choice(KAC)
                        G = bot.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bot.updateGroup(G)
                        Ticket = bot.reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        bot.updateGroup(G)
                    except:
                        try:
                            bot = random.choice(KAC)
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot.updateGroup(G)
                            Ticket = bot.reissueGroupTicket(op.param1)
                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.preventedJoinByTicket = True
                            bot.updateGroup(G)
                        except:
                            try:
                                bot = random.choice(KAC)
                                G = bot.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                bot.updateGroup(G)
                                Ticket = bot.reissueGroupTicket(op.param1)
                                client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G.preventedJoinByTicket = True
                                bot.updateGroup(G)
                            except:
                                try:
                                    bot = random.choice(KAC)
                                    G = bot.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    bot.updateGroup(G)
                                    Ticket = bot.reissueGroupTicket(op.param1)
                                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G.preventedJoinByTicket = True
                                    bot.updateGroup(G)
                                except:
                                    try:
                                        bot = random.choice(KAC)
                                        G = bot.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        bot.updateGroup(G)
                                        Ticket = bot.reissueGroupTicket(op.param1)
                                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        bot.updateGroup(G)
                                    except:
                                        try:
                                            bot = random.choice(KAC)
                                            G = bot.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            bot.updateGroup(G)
                                            Ticket = bot.reissueGroupTicket(op.param1)
                                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            bot.updateGroup(G)
                                        except:
                                            try:
                                                bot = random.choice(KAC)
                                                G = bot.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                bot.updateGroup(G)
                                                Ticket = bot.reissueGroupTicket(op.param1)
                                                client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                G.preventedJoinByTicket = True
                                                bot.updateGroup(G)
                                            except:
                                                try:
                                                    bot = random.choice(KAC)
                                                    G = bot.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    bot.updateGroup(G)
                                                    Ticket = bot.reissueGroupTicket(op.param1)
                                                    client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    G.preventedJoinByTicket = True
                                                    bot.updateGroup(G)
                                                except:
                                                    pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass

        else:
            if op.param3 in haveP:
                if op.param2 in haveP:
                    try:
                        bot = random.choice(KAC)
                        bot.findAndAddContactsByMid(op.param3)
                        bot.inviteIntoGroup(op.param1,[op.param3])
                    except Exception as e:
                        print (e)
                else:
                    sendMessage(op.param1, "権限保有者を退会させたため、強制退出を試みます。")
                    try:
                        bot = random.choice(KAC)
                        bot.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            bot = random.choice(KAC)
                            bot.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                    bot = random.choice(KAC)
                    bot.findAndAddContactsByMid(op.param3)
                    bot.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('black.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    G = client.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    client.updateGroup(G)
            else:
                if op.param1 in res['us']:
                    if op.param2 == res['us'][op.param1]:
                        res['num'][op.param1] += 1
                    else:
                        del res['num'][op.param1]
                        del res['us'][op.param1]
                        res['us'][op.param1] = op.param2
                        res['num'][op.param1] = 1
                else:
                    res['us'][op.param1] = op.param2
                    res['num'][op.param1] = 1
                if op.param1 in wait["PROTECTKICK"]:
                    if op.param1 in res['num']:
                        if res['num'][op.param1] >= 1:
                            if(op.param2 in bots) or (op.param2 in haveP):
                                del res['num'][op.param1]
                                del res['us'][op.param1]
                            else:
                                try:
                                    bot = random.choice(KAC)
                                    bot.kickoutFromGroup(op.param1, [op.param2])
                                except:
                                    bot = random.choice(KAC)
                                    bot.kickoutFromGroup(op.param1,[op.param2])
                                sendMessage(op.param1, "蹴り保護がオンになっています")
                                wait["PROTECTURLINVITECHANGE"][op.param1] = True
                                G = client.getGroup(op.param1)
                                if G.preventJoinByTicket == False:
                                    G.preventJoinByTicket = True
                                    client.updateGroup(G)
                                else:
                                    pass
                                if op.param2 in wait["blacklist"]:
                                    pass
                                else:
                                    wait["blacklist"][op.param2] = True
                                    f=codecs.open('black.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                del res['num'][op.param1]
                                del res['us'][op.param1]
                elif op.param1 in res['num']:
                    if res['num'][op.param1] >= 3:
                        if(op.param2 in bots) or (op.param2 in haveP):
                            del res['num'][op.param1]
                            del res['us'][op.param1]
                        else:
                            try:
                                bot = random.choice(KAC)
                                bot.kickoutFromGroup(op.param1, [op.param2])
                            except:
                                bot = random.choice(KAC)
                                bot.kickoutFromGroup(op.param1,[op.param2])
                            sendMessage(op.param1, "3回連続で退会させたことを検知しました。")
                            wait["PROTECTURLINVITECHANGE"][op.param1] = True
                            G = client.getGroup(op.param1)
                            if G.preventJoinByTicket == False:
                                G.preventJoinByTicket = True
                                client.updateGroup(G)
                            else:
                                pass
                            if op.param2 in wait["blacklist"]:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                                f=codecs.open('black.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            del res['num'][op.param1]
                            del res['us'][op.param1]
    except Exception as e:
        print (e)
clientPoll.addOpInterrupt(19, NOTIFIED_KICKOUT_FROM_GROUP)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 13:
            try:
                if msg.to in wait["rapidFire"]:
                    if msg._from in admins:
                        pass
                    elif time.time() - wait["rapidFire"][msg.to] < 3:
                        return
                    else:
                        wait["rapidFire"][msg.to] = time.time()
                else:
                    wait["rapidFire"][msg.to] = time.time()
                if msg.to in wait['readPoint']:
                    if msg._from in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg._from]
                if msg.to in offbot:
                    return
                if msg._from in wait["blacklist"]:
                    return
                elif msg.to in wait["kick"]:
                    if(msg.to in wait["wblacklist"]):
                        del wait["wblacklist"][msg.to]
                    if(msg.to in wait["wdblacklist"]):
                        del wait["wdblacklist"][msg.to]
                    if (msg._from in (admins + p1 + p2)):
                        target = msg.contentMetadata["mid"]
                        if (target in haveP) or (target in bots):
                            sendMessage(msg.to,"権限保持者なので退会させることはできません。")
                        else:
                            try:
                                KickerD.kickoutFromGroup(msg.to,[target])
                            except:
                                try:
                                    KickerF.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                        del wait["kick"][msg.to]
                    else:
                        pass
                elif msg.to in wait["wblacklist"]:
                    if(msg.to in wait["wdblacklist"]):
                        del wait["wdblacklist"][msg.to]
                    if(msg.to in wait["kick"]):
                        del wait["kick"][msg.to]
                    if(msg._from in (admins + p1)):
                        target = msg.contentMetadata["mid"]
                        if (target in haveP) or (target in bots):
                            sendMessage(msg.to,"ブラックリストに追加できないユーザーです。")
                            del wait["wblacklist"][msg.to]
                        else:
                            if target in wait["blacklist"]:
                                sendMessage(msg.to,"既にブラックリストに登録されています。")
                                del wait["wblacklist"][msg.to]
                            else:
                                wait["blacklist"][target] = True
                                sendMessage(msg.to,"ブラックリストに追加しました。")
                                del wait["wblacklist"][msg.to]
                                wait["blacklist"][target] = True
                                f=codecs.open('black.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        sendMessage(msg.to,"あなたには権限がありません。")
                elif msg.to in wait["wdblacklist"]:
                    if(msg.to in wait["wblacklist"]):
                        del wait["wblacklist"][msg.to]
                    if(msg.to in wait["kick"]):
                        del wait["kick"][msg.to]
                    if(msg._from in (p1 + admins)):
                        target = msg.contentMetadata["mid"]
                        if(target in wait["blacklist"]):
                            del wait["blacklist"][target]
                            sendMessage(msg.to,"ブラックリストから削除しました。")
                            f=codecs.open('black.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        else:
                            sendMessage(msg.to,"ブラックリストに登録されていません。")
                    else:
                        sendMessage(msg.to,"あなたには権限がありません。")
                    del wait["wdblacklist"][msg.to]
                elif 'displayName' in msg.contentMetadata:
                    contact = client.getContact(msg.contentMetadata["mid"])
                    if(msg.contentMetadata["mid"] in wait["blacklist"]):
                        bll = "True"
                    else:
                        bll = "False"
                    sendMessage(msg.to, "[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus +"\n[ブラックリスト]:\n" + bll)
                else:
                    if(msg.contentMetadata["mid"] in wait["blacklist"]):
                        bll = "True"
                    else:
                        bll = "False"
                    contact = client.getContact(msg.contentMetadata["mid"])
                    sendMessage(msg.to, "[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ブラックリスト]:\n" + bll)
            except:
                sendMessage(msg.to,"残念ですが、ユーザーが存在しませんでした。")

        elif msg.contentType == 16:
            if msg.to in wait["rapidFire"]:
                if msg._from in admins:
                    pass
                elif time.time() - wait["rapidFire"][msg.to] < 3:
                    return
                else:
                    wait["rapidFire"][msg.to] = time.time()
            else:
                wait["rapidFire"][msg.to] = time.time()
            if msg.to in wait['readPoint']:
                if msg._from in wait["ROM"][msg.to]:
                    del wait["ROM"][msg.to][msg._from]
            if msg.to in offbot:
                return
            if msg._from in wait["blacklist"]:
                return
            elif 'text' not in msg.contentMetadata:
                if 'mediaOid' in msg.contentMetadata:
                    Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                    if msg.contentMetadata['mediaType'] == 'V':
                        if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                        else:
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                    else:
                        if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                        else:
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                elif 'stickerId' in msg.contentMetadata:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                    else:
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                else:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
                    else:
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
            else:
                if 'mediaOid' in msg.contentMetadata:
                    Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                    if msg.contentMetadata['mediaType'] == 'V':
                       if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                       else:
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                    else:
                        if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                        else:
                            sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                elif 'stickerId' in msg.contentMetadata:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                    else:
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                else:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])
                    else:
                        sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])

        elif msg.contentType == 0:
            if msg.to in wait["rapidFire"]:
                if msg._from in admins:
                    pass
                elif time.time() - wait["rapidFire"][msg.to] < 3:
                    return
                else:
                    wait["rapidFire"][msg.to] = time.time()
            else:
                wait["rapidFire"][msg.to] = time.time()
            if msg._from in wait["blacklist"]:
                return
            if msg.to in wait['readPoint']:
                if msg._from in wait["ROM"][msg.to]:
                    del wait["ROM"][msg.to][msg._from]
                    #print "送信されたのでROM削除->" + msg._from
            if cms(msg.text, ["sleep"]):
                if msg.to not in offbot:
                    sendMessage(msg.to, "ミュートにしました")
                    offbot.append(msg.to)
                else:
                    sendMessage(msg.to, "すでにミュートですよ。")
            elif cms(msg.text, ["get up"]):
                if msg.to in offbot:
                    sendMessage(msg.to, "おはようございます、気持ちの良い朝ですね！")
                    offbot.remove(msg.to)
                else:
                    sendMessage(msg.to, "どうかされましたか？")
            if msg.to in offbot:
                return
            elif cmd(msg.text, ["Y","y","おk","N","n","だめ"]):
                if msg._from == wait['bye'][msg.to]:
                    if cmd(msg.text, ["Y","いいよ","y","おk"]):
                        sendMessage(msg.to, "また会える日を楽しみにしています。")
                        client.leaveGroup(msg.to)
                        for bot in KAC:
                            bot.leaveGroup(msg.to)
                        del wait['bye'][msg.to]
                    elif cmd(msg.text, ["N","n","だめ"]):
                        sendMessage(msg.to, "ありがとうございます。まだご主人様と一緒にいられるのですね。")
                        del wait['bye'][msg.to]
                else:
                    pass
            elif cms(msg.text, ["終了"]):
                if msg._from in admins:
                    f=codecs.open('black.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    sendMessage(msg.to, "設定ファイルの保存が完了")
                    sendMessage(msg.to, "また、会いましょうね。")
                    sys.exit(0)
                else:
                    sendMessage(msg.to, "申し訳ございません。あなたには権限がありません。")
            elif cms(msg.text,["保存"]):
                if msg._from in admins:
                    f=codecs.open('black.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    f=codecs.open('protect.json','w','utf-8')
                    json.dump(wait["protect"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    f=codecs.open('PROTECTKICK.json','w','utf-8')
                    json.dump(wait["PROTECTKICK"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    f=codecs.open('PROTECTURLINVITECHANGE.json','w','utf-8')
                    json.dump(wait["PROTECTURLINVITECHANGE"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    sendMessage(msg.to, "設定ファイルの保存が完了")

                else:
                    sendMessage(msg.to, "申し訳ございません。あなたには権限がありません。")
            elif cms(msg.text, ["ねむい","眠たい","ねむたい"]):
                AABB = [1,2,3,4,5,6]
                AAC = random.choice(AABB)
                if 4 <= AAC:
                    pass
                elif 3 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "眠い時は寝てもいいのですよ？" + name + "さん")
                elif 2 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to,name + "さん、無理せずに寝ちゃいましょう！")
                elif 1 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "もう寝なさい")
            elif cms(msg.text, ["おやすみ","おやすみなさい","ねます","寝ます"]):
                AABB = [1,2,3,4,5,6]
                AAC = random.choice(AABB)
                if 4 <= AAC:
                    pass
                elif 3 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "おやすみなさい！" + name + "さん")
                elif 2 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to,name + "さん、ごゆっくり！")
                elif 1 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "もう寝てしまうのですか？")
            elif msg.text.lower().startswith("レタス"):
                AABB = [1,2,3,4,5,6,7,8]
                AAC = random.choice(AABB)
                if 4 <= AAC:
                    pass
                elif 3 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "呼びましたか？" + name + "さん")
                elif 2 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to,name + "さん、なんでしょう")
                elif 1 == AAC:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "( 'ω')ふぁっ")
            elif cms(msg.text, ["さようなら"]):
                if (msg._from in haveP):
                    sendMessage(msg.to, "本当にいいのですか・・・？\n(y/n)")
                    wait['bye'][msg.to] = msg._from
                    #print wait
                else:
                    sendMessage(msg.to,"申し訳ございません。あなたには権限がありません。")

            elif cms(msg.text,["ブラックリスト追加"]):
                if(msg._from in (admins + p1)):
                    sendMessage(msg.to,"ブラックリストに追加する連絡先を送信してください。")
                    wait["wblacklist"][msg.to] = True
                else:
                    sendMessage(msg.to,"あなたには権限がありません。")
            elif cms(msg.text,["ブラックリスト削除"]):
                if(msg._from in (admins + p1)):
                    sendMessage(msg.to,"ブラックリストから削除する連絡先を送信してください。")
                    wait["wdblacklist"][msg.to] = True
                else:
                    sendMessage(msg.to,"あなたには権限がありません。")
            elif cms(msg.text, ["既読ポイント設定"]):
                if (msg._from in haveP):
                    sendMessage(msg.to, "既読ポイントを設定しました。\n確認したい場合は「既読確認」と送信してください。")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    #print wait

            elif cms(msg.text, ["既読確認"]):
                if (msg._from in haveP):
                    if msg.to in wait['readPoint']:
                        if wait["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        sendMessage(msg.to, "既読を付けた人は%s\nです！\n\n既読無視している人は\n%sです！\n\n既読ポイント作成日時:\n[%s]\n\n\n既読無視している人とは、既読ポイント作成時以降、既読しているのにも関わらず一度も発言していない人を指します。" % (wait['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        sendMessage(msg.to, "既読ポイントが設定されていません。")

            elif cms(msg.text,["メンバーチェック"]):
                group = client.getGroup(msg.to)
                gMembMids = [contact.mid for contact in group.members]
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, gMembMids)
                cocoa = ""
                for mm in matched_list:
                    try:
                        cocoa += client.getContact(mm).displayName + "\n"
                    except Exception as error:
                        try:
                            sendMessage(msg.to,str(error))
                        except:
                            pass
                if cocoa == "":
                    sendMessage(msg.to,"ブラックリストに入っているユーザーはいません。")
                else:
                    sendMessage(msg.to,cocoa + "がブラックリストです。")
            #elif cms(msg.text, ["mid"]):
                #sendMessage(msg.to, msg._from)
            #elif cms(msg.text, ["gid"]):
                #sendMessage(msg.to, msg.to)
            elif cms(msg.text, ["保護 名前","保護　名前"]):
                if (msg._from in haveP):
                    if msg.to in wait["PROTECTGNAMECHANGE"]:
                        sendMessage(msg.to, "すでにグループ名の変更は禁止されています。")
                    else:
                        wait["PROTECTGNAMECHANGE"][msg.to] = client.getGroup(msg.to).name
                        #print wait
                        sendMessage(msg.to, "グループ名の変更を禁止しました。")
            elif cms(msg.text, ["保護 名前 オフ","保護　名前　オフ"]):
                if (msg._from in haveP):
                    if msg.to in wait["PROTECTGNAMECHANGE"]:
                        del wait["PROTECTGNAMECHANGE"][msg.to]
                        # wait
                        sendMessage(msg.to, "グループ名の変更を許可しました。")
                    else:
                        sendMessage(msg.to, "すでにグループ名の変更は許可されています。")
                else:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "ごめんなさい、" + name + "さんには実行する権限がありません。")
            elif cms(msg.text, ["保護 URL","保護　URL"]):
                if (msg._from in haveP):
                    if msg.to in wait["PROTECTURLINVITECHANGE"]:
                        sendMessage(msg.to, "すでにURL招待設定の変更は禁止されています。")
                    else:
                        wait["PROTECTURLINVITECHANGE"][msg.to] = True
                        #print wait
                        G =client.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        client.updateGroup(G)
                        sendMessage(msg.to, "URL招待設定の変更を禁止しました。")
                        f=codecs.open('PROTECTURLINVITECHANGE.json','w','utf-8')
                        json.dump(wait["PROTECTURLINVITECHANGE"], f, sort_keys=True, indent=4,ensure_ascii=False)
            elif cms(msg.text, ["保護 URL オフ","保護　URL　オフ"]):
                if (msg._from in haveP):
                    if msg.to in wait["PROTECTURLINVITECHANGE"]:
                        del wait["PROTECTURLINVITECHANGE"][msg.to]
                        #print wait
                        sendMessage(msg.to, "URL招待設定の変更を許可しました。")
                        f=codecs.open('PROTECTURLINVITECHANGE.json','w','utf-8')
                        json.dump(wait["PROTECTURLINVITECHANGE"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        sendMessage(msg.to, "すでにURL招待設定の変更は許可されています。")
                else:
                    name = client.getContact(msg._from).displayName
                    sendMessage(msg.to, "ごめんなさい、" + name + "さんには実行する権限がありません。")
            elif cms(msg.text, ["保護 蹴り","保護　蹴り"]):
                if (msg._from in haveP):
                    if msg.to in wait["PROTECTKICK"]:
                        sendMessage(msg.to, "すでに強制退会は禁止されています。")
                    else:
                        wait["PROTECTKICK"][msg.to] = True
                        #print wait
                        sendMessage(msg.to, "強制退会を禁止しました。")
                        f=codecs.open('PROTECTKICK.json','w','utf-8')
                        json.dump(wait["PROTECTKICK"], f, sort_keys=True, indent=4,ensure_ascii=False)
            elif cms(msg.text, ["保護 蹴り オフ","保護　蹴り　オフ"]):
                if (msg._from in haveP):
                    if msg.to in wait["PROTECTKICK"]:
                        del wait["PROTECTKICK"][msg.to]
                        #print wait
                        sendMessage(msg.to, "連続でない強制退会を許可しました。")
                        f=codecs.open('PROTECTKICK.json','w','utf-8')
                        json.dump(wait["PROTECTKICK"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        sendMessage(msg.to, "すでに連続でない強制退会は許可されています。")
            elif cms(msg.text, ["group"]):
                if (msg._from in haveP):
                    try:
                        group = client.getGroup(msg.to)
                        md = "[グループ名]: " + group.name + "\n\n[gid]: " + group.id + "\n\n[アイコン画像]: \nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                        if group.preventedJoinByTicket is False: md += "\n\n招待URL: 許可中です\n"
                        else: md += "\n\n招待URL: 拒否中です\n"

                        if group.invitee is None: md += "\nメンバー数: " + str(len(group.members)) + "人\n招待中: 0人"
                        else: md += "\nメンバー数: " + str(len(group.members)) + "人\n招待中: " + str(len(group.invitee)) + "人"

                        if msg.to in wait["PROTECTURLINVITECHANGE"]: md += "\n\n保護 URL: オン"
                        else: md += "\n\n保護 URL: オフ"

                        if msg.to in wait["PROTECTGNAMECHANGE"]: md += "\n\n保護 グループ名: オン"
                        else: md += "\n\n保護 グループ名: オフ"

                        if msg.to in wait["PROTECTKICK"]: md += "\n\n保護 蹴り: オン"
                        else: md += "\n\n保護 蹴り: オフ"
                        client.sendMessage(msg.to, md)
                    except:
                        sendMessage(msg.to,"残念ですが、エラーが発生しました。")
                elif cms(msg.text, ["USER","user","User","ユーザー"]):
                    try:
                        contact = client.getContact(msg._from)
                        sendMessage(msg.to, "[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg._from + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus)
                    except:
                        sendMessage(msg.to,"残念ですが、エラーが発生しました。")
            elif cms(msg.text, ["招待URL許可"]):
                if (msg._from in haveP):
                    group = client.getGroup(msg.to)
                    if group.preventedJoinByTicket == False:
                        client.sendMessage(msg.to, "既に許可されています。")
                    else:
                        group.preventedJoinByTicket = False
                        client.updateGroup(group)
                        client.sendMessage(msg.to, "URL招待を許可しました。")
            elif cms(msg.text, ["招待URL拒否"]):
                if (msg._from in haveP):
                    group = client.getGroup(msg.to)
                    if group.preventedJoinByTicket == True:
                        client.sendMessage(msg.to, "既に拒否されています")
                    else:
                        group.preventedJoinByTicket = True
                        client.updateGroup(group)
                        client.sendMessage(msg.to, "URL招待を拒否しました")
            elif cms(msg.text, ["gurl_get","Gurl_Get","GURL_GET","招待URL生成"]):
                if (msg._from in haveP):
                    g = client.getGroup(msg.to)
                    if g.preventedJoinByTicket == True:
                        g.preventedJoinByTicket = False
                        client.updateGroup(g)
                    gurl = client.reissueGroupTicket(msg.to)
                    sendMessage(msg.to,"line://ti/g/" + gurl)
            elif "キッカー補充" == msg.text:
                if (msg._from in haveP):
                    G=client.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    client.updateGroup(G)
                    Ti=client.reissueGroupTicket(msg.to)
                    for x in KAC:
                        x.acceptGroupInvitationByTicket(msg.to,Ti)
                    X=client.getGroup(msg.to)
                    X.preventedJoinByTicket = True
            elif "bot補充" == msg.text:
                if (msg._from in haveP):
                    bot = random.choice(KAC)
                    G = bot.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    bot.updateGroup(G)
                    Ticket = bot.reissueGroupTicket(msg.to)
                    client.acceptGroupInvitationByTicket(msg.to,Ticket)
                    X=bot.getGroup(msg.to)
                    X.preventedJoinByTicket = True
            elif cms(msg.text, ["help","ヘルプ","へるぷ"]):
                if (msg._from in haveP):
                    text = """レタスbot
【コマンド一覧】
[help]→ヘルプを出します
[sleep]→botを反応させなくします
[get up]→botが反応するようにします
[キッカー補充]→キッカーを補充します
[みんな返事して！]→botの点呼をします
[さようなら]→botを抜かします
[group]→グループの情報を出します
[user]→実行したユーザーの情報を出します
[招待URL許可]→URLを許可します
[招待URL拒否]→URLを拒否します
[招待URL生成]→URLを出します
[mk:@メンション]→メンションでキックします
[kick]→指定したアカウントをキックします
[権限]→権限を確認します
【保護】
[保護 名前]→グループ名の変更を禁止します
[保護 名前 オフ]→グループ名の変更を許可します
[保護 URL]→招待URLを禁止します
[保護 URL オフ]→招待URLを許可します
[保護 蹴り]→強制退会を禁止します
[保護 蹴りオフ]→連続でない強制退会を許可します
【ブラックリスト】(権限によっては使えません)
[ブラックリスト追加]→ブラックリストに追加します
[ブラックリスト削除]→ブラックリストから削除します
[メンバーチェック]→ブラックリストがグループに居るか確認します
[ブラックリスト確認]→ブラックリストの人を確認します
[ブラックリスト確認 -c]→ブラックリストの人を連絡先で確認します
[ブラリス排除]→ブラックリストの人をグループから蹴ります
【その他機能】
[既読ポイント設定]既読ポイントを設定します
[既読確認]既読ポイントに既読をつけた人と既読無視してる人の名前を出します
タイムラインを共有、ノート投稿、アルバム作成、連絡先をおくるとその情報を表示します"""
                    sendMessage(msg.to, text)
            elif cms(msg.text, ["help2","ヘルプ2","へるぷ2"]):
                if (msg._from in haveP):
                    path = "C:/Users/11451/Downloads/selfBOT-master/help.txt"
                    client.sendFile(msg.to, path)
            elif cms(msg.text, ["みんな返事して！"]):
                if (msg._from in haveP):
                    client.sendMessage(msg.to,"いくよー!!")
                    client.sendMessage(msg.to,"点呼1!")
                    KB.sendMessage(msg.to,"点呼2!")
                    KC.sendMessage(msg.to,"点呼3!")
                    KD.sendMessage(msg.to,"点呼4!")
                    KE.sendMessage(msg.to,"点呼5!")
                    KF.sendMessage(msg.to,"点呼6!")
                    KG.sendMessage(msg.to,"点呼7!")
                    KH.sendMessage(msg.to,"点呼8!")
                    KI.sendMessage(msg.to,"点呼9!")
                    KJ.sendMessage(msg.to,"点呼10!")
                    client.sendMessage(msg.to,"みんないるね!")
            elif msg.text.lower().startswith("mk: "):
                if (msg._from in haveP):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            bot = random.choice(KAC)
                            bot.kickoutFromGroup(msg.to,[target])
                        except:
                            client.sendMessage(msg.to,"Error")
            elif cms(msg.text, ["test"]):
                if (msg._from in haveP):
                    sendMessage(msg.to,"test")
            elif cms(msg.text,["kick"]):
                if (msg._from in (admins + p1 + p2)):
                    wait["kick"][msg.to] = True
                    #print wait
                    sendMessage(msg.to,"対象のアカウントを貼ってください。")
                else:
                    sendMessage(msg.to,"あなたには権限がありません")
            elif cms(msg.text,["全部抜けろ"]):
                if(msg._from in admins):
                    for gid in client.getGroupIdsJoined():
                        client.leaveGroup(gid)
                        KickerB.leaveGroup(gid)
                        KickerC.leaveGroup(gid)
            elif cms(msg.text,["全部キャンセルしろ"]):
                if(msg._from in admins):
                    for gid in client.getGroupIdsInvited():
                        client.rejectGroupInvitation(gid)
                    sendMessage(msg.to,"キャンセル完了しました。")
            elif cms(msg.text,["権限"]):
                if msg._from in admins:
                    sendMessage(msg.to,"あなたは最高権限者です。")
                elif msg._from in p1:
                    sendMessage(msg.to,"あなたはレベル3の権限を所持しています。")
                elif msg._from in p2:
                    sendMessage(msg.to,"あなたはレベル2の権限を所持しています。")
                elif msg._from in p3:
                    sendMessage(msg.to,"あなたはレベル1の権限を所持しています。")
                else:
                    sendMessage(msg.to,"あなたは権限を所持していません。")
            elif cms(msg.text,["ブラックリスト確認"]):
                if msg._from in (admins):
                    if wait["blacklist"] == {}:
                        sendMessage(msg.to,"ブラックリストにしている人はいません。")
                    else:
                        sendMessage(msg.to,"以下がブラックリストです。")
                        mc = ""
                        for mi_d in wait["blacklist"]:
                            try:
                                mc += "・" +client.getContact(mi_d).displayName + "\n"
                            except Exception as error:
                                sendMessage(msg.to,str(error))
                        sendMessage(msg.to,mc)
            elif cms(msg.text,["ブラックリスト確認 -c"]):
                if msg._from in (admins):
                    if wait["blacklist"] == {}:
                        sendMessage(msg.to,"ブラックリストにしている人はいません。")
                    else:
                        sendMessage(msg.to,"以下がブラックリストです。")
                        for mi_d in wait["blacklist"]:
                            try:
                                client.sendMessage(msg.to,None,contentMetadata = {"mid":mi_d},contentType = 13)
                            except Exception as error:
                                sendMessage(msg.to,str(error))
            elif msg.text in ["愛のプレゼント","愛的禮物"]:
                if msg._from in (admins):
                    sendMessage(msg.to,None,contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020','PRDTYPE': 'THEME','MSGTPL': '5'},contentType = 9)
            elif cms(msg.text,["ブラリス排除"]):
                if(msg._from in (admins + p1)):
                    group = client.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        sendMessage(msg.to,"ブラックリストユーザーはいませんでした。")
                        return
                    for jj in matched_list:
                        try:
                            client.kickoutFromGroup(msg.to,[jj])
                        except:
                            bot = random.choice(KAC)
                            bot.kickoutFromGroup(msg.to,[jj])
                    sendMessage(msg.to,"ブラックリストユーザーの追い出しが完了しました。")
            elif cms(msg.text, ["speed"]):
                if (msg._from in haveP):
                    start = time.time()
                    client.sendMessage(msg.to, "計測中です...")
                    elapsed_time = time.time() - start
                    client.sendMessage(msg.to, "返信速度計測結果\n>>%s秒" % (elapsed_time))

    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print (error)

clientPoll.addOpInterrupt(26, RECEIVE_MESSAGE)

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name + "さん\n" + datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                wait['ROM'][op.param1][op.param2] = "・" + Name + "さん"
        else:
            pass
    except:
        pass

clientPoll.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        if profile.mid in op.param3:
            if op.param2 in haveP:
                client.acceptGroupInvitation(op.param1)
                G = client.getGroup(op.param1)
                G.preventedJoinByTicket = False
                client.updateGroup(G)
                Ticket = client.reissueGroupTicket(op.param1)
                for bot in KAC:
                    bot.acceptGroupInvitationByTicket(op.param1,Ticket)
                G.preventedJoinByTicket = True
                client.updateGroup(G)
                client.sendMessage(op.param1, "よろしく^^:")
                wait["rapidFire"][op.param1] = time.time()
        elif op.param1 in wait["protect"]:
            if op.param2 in ki:
                return
            if (op.param2 in haveP):
                return
            Inviter = op.param3.replace("",',')
            InviterX = Inviter.split(",")
            client.cancelGroupInvitation(op.param1, InviterX)
            try:
                bot = random.choice(KAC)
                bot.kickoutFromGroup(op.param1,[op.param2])
            except:
                try:
                    bot = random.choice(KAC)
                    bot.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
            bot = random.choice(KAC)
            bot.sendMessage(op.param1,"ブラリスっぽい")

        else:
            Inviter = op.param3.replace("",',')
            InviterX = Inviter.split(",")
            matched_list = []
            for tag in wait["blacklist"]:
                matched_list+=filter(lambda str: str == tag, InviterX)
            if matched_list == []:
                pass
            else:
                client.cancelGroupInvitation(op.param1, matched_list)
                if op.param2 in haveP+bots:
                    return
                try:
                    bot = random.choice(KAC)
                    bot.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        bot = random.choice(KAC)
                        bot.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                bot = random.choice(KAC)
                bot.sendMessage(op.param1,"ブラリスが招待されたので招待者をキックしました")
    except Exception as e:
        print (e)

def NOTIFIED_UPDATE_GROUP(op):
    try:
        #print op
        """
        op.param3
        1がグループ名
        2がグループ画像
        3が
        4がurl
        """
        #wait["PROTECTGNAMECHANGE"]
        if op.param3 == "1":
            if op.param2 in bots:
                return
            if op.param1 in wait["PROTECTGNAMECHANGE"]:
                if (op.param2 in haveP):
                    G =client.getGroup(op.param1)
                    G.name = gname[op.param1]
                    client.updateGroup(G)
                else:
                    G = client.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    G.name = gname[op.param1]
                    client.updateGroup(G)
                    try:
                        bot = random.choice(KAC)
                        bot.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            bot = random.choice(KAC)
                            bot.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        elif op.param3 == "4":
            if op.param2 in bots:
                return
            if op.param1 in wait["PROTECTURLINVITECHANGE"]:
                if (op.param2 in haveP):
                    G = KB.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    KB.updateGroup(G)
                else:
                    G = client.getGroup(op.param1)
                    if G.preventedJoinByTicket == True:
                        pass
                    else:
                        try:
                            bot = random.choice(KAC)
                            bot.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                bot = random.choice(KAC)
                                bot.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                        G.preventedJoinByTicket = False
                        client.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        G.preventedJoinByTicket = False
                        client.updateGroup(G)
    except Exception as e:
        print (e)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
    try:
        if op.param2 in wait["blacklist"]:
            if op.param2 in bots:
                return
            G = client.getGroup(op.param1)
            try:
                bot = random.choice(KAC)
                bot.kickoutFromGroup(op.param1,[op.param2])
            except:
                try:
                    bot = random.choice(KAC)
                    bot.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
            G.preventedJoinByTicket = True
            client.updateGroup(G)
    except Exception as e:
        print (e)

clientPoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE,
    OpType.NOTIFIED_KICKOUT_FROM_GROUP: NOTIFIED_KICKOUT_FROM_GROUP,
    OpType.NOTIFIED_UPDATE_GROUP: NOTIFIED_UPDATE_GROUP,
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.NOTIFIED_ACCEPT_GROUP_INVITATION: NOTIFIED_ACCEPT_GROUP_INVITATION,
})


while True:
    clientPoll.trace()
