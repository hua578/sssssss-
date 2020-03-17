import LINEPY
from LINEPY import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
#import pyimgflip
from googletrans import Translator
import youtube_dl
#ANTIJS_V2
#===================
print ("======[ MEMBUAT AKUN B❂TTR❂X Bots]======")
print ("===========[ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ]=============")
#cl = LineClient()
cl = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))
print ("AKUN BOTTROX BOTS 1")
#ki = LineClient()
ki = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))
print ("AKUN BOTTROX BOTS 2")
#kk = LineClient()
kk = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))
print ("AKUN BOTTROX BOTS 3")
#kc = LineClient()
kc = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))
print ("AKUN BOTTROX BOTS 4")
#kb = LineClient()
kb = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
kb.log("Auth Token : " + str(kb.authToken))
channel4 = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel4.channelAccessToken))
print ("AKUN BOTTROX BOTS 5")
#kd = LineClient()
kd = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
kd.log("Auth Token : " + str(kd.authToken))
channel5 = LineChannel(kd)
kd.log("Channel Access Token : " + str(channel5.channelAccessToken))
print ("AKUN BOTTROX BOTS 6")
#ke = LineClient()
ke = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
ke.log("Auth Token : " + str(ke.authToken))
channel6 = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel6.channelAccessToken))
print ("AKUN BOTTROX BOTS 7")
#kf = LineClient()
kf = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
kf.log("Auth Token : " + str(kf.authToken))
channel7 = LineChannel(kf)
kf.log("Channel Access Token : " + str(channel7.channelAccessToken))
print ("AKUN BOTTROX BOTS 8")
#kg = LineClient()
kg = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
kg.log("Auth Token : " + str(kg.authToken))
channel8 = LineChannel(kg)
kg.log("Channel Access Token : " + str(channel8.channelAccessToken))
print ("AKUN B͞o͞t͞T͞r͞o͞x͞ᴮᴼᵀˢ BOTS 9")
#kh = LineClient()
kh = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
kh.log("Auth Token : " + str(kh.authToken))
channel9 = LineChannel(kh)
kh.log("Channel Access Token : " + str(channel9.channelAccessToken))
print ("AKUN GHOTS 1")
#satria = LineClient()
satria = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
satria.log("Auth Token : " + str(satria.authToken))
channel10 = LineChannel(satria)
satria.log("Channel Access Token : " + str(channel10.channelAccessToken))
print ("AKUN ANTIJSNYA")
#sw = LineClient()
sw = LineClient(authToken='EFJTzjjyM6qK83TuXbzf.MJLhO5r7vO8MsXweQmErVW.XTYcpjXk5eQ0boKL/dRTQOBaOmfW1V/VZTiOLWwDNvI=')
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))
print ("╔══╗─╔═══╗╔════╗╔════╗╔═══╗╔═══╗╔═╗╔═╗")
print ("║╔╗║─║╔═╗║║╔╗╔╗║║╔╗╔╗║║╔═╗║║╔═╗║╚╗╚╝╔╝")
print ("║╚╝╚╗║║─║║╚╝║║╚╝╚╝║║╚╝║╚═╝║║║─║║─╚╗╔╝─")
print ("║╔═╗║║║─║║──║║────║║──║╔╗╔╝║║─║║─╔╝╚╗─")
print ("║╚═╝║║╚═╝║──║║────║║──║║║╚╗║╚═╝║╔╝╔╗╚╗")
print ("╚═══╝╚═══╝──╚╝────╚╝──╚╝╚═╝╚═══╝╚═╝╚═╝")
print ("======⊰์◉⊱B❂T$ SIAP DI GUNAKAN⊰์◉⊱=======")


poll = LinePoll(cl)
call = cl
creator = ["u1608ae21e5de2547b5fa8707b21ca220"]
owner = ["u1608ae21e5de2547b5fa8707b21ca220"]
admin = ["u1608ae21e5de2547b5fa8707b21ca220"]
staff = ["u1608ae21e5de2547b5fa8707b21ca220"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = kd.getProfile().mid
Fmid = ke.getProfile().mid
Gmid = kf.getProfile().mid
Imid = kg.getProfile().mid
Jmid = kh.getProfile().mid
Hmid = satria.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc,kb,kd,ke,kf,kg,kh]
ABC = [ki,kk,kc,kb,kd,ke,kf,kg,kh]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Imid,Jmid,Hmid,Zmid]
Satria = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []

responsename0 = cl.getProfile().displayName
responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName
responsename5 = kd.getProfile().displayName
responsename6 = ke.getProfile().displayName
responsename7 = kf.getProfile().displayName
responsename8 = kg.getProfile().displayName
responsename9 = kh.getProfile().displayName
responsename10 = satria.getProfile().displayName
responsename11 = sw.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":True,
    "dblacklist":True,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    'autoJoin':True,
    'autoAdd':False,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"SINI KAK GABUNG CHAT AJA ðŸ˜Š",
    "Respontag":"SEKAARNG TAG BESOK JATUH CINTA",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like by line.me/ti/p/~iia008",
    "message":"Terimakasih sudah add saya ",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)      
with open('staff.json', 'r') as fp:
    staff = json.load(fp)          
    
Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '\n🇲🇨 %02d Hari \n🇲🇨 %02d Jam \n🇲🇨 %02d Menit \n🇲🇨 %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '\n🇲🇨 %02d Hari \n🇲🇨 %02d Jam \n🇲🇨 %02d Menit \n🇲🇨 %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(ki.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers1(to, mids=[]):
  #  if mid in mids: mids.remove(mid)
    parsed_len = len(mids)//20+1
    result = '╭───「 ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ 」\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            cl.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''
        
def mentionMembers2(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(ki.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@BotTroxᴮᴼᵀ "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMeention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@BotTroxᴮᴼᵀ "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Haiiii...  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        ki.sendMessage(to, None, contentMetadata={"STKID":"51626525","STKPKGID":"11538","STKVER":"1"}, contentType=7)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Haiii...  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = ki.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(ki.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Byee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = ki.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(ki.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))        
        
def sendMentionV2(to, text="", mids=[], name="", url="", iconlink=""):
    arrData = ""
    arr = []
    mention = "@BotTroxᴮᴼᵀ "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 9
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 9
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink },0)

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = ki.getAllContactIds()
        gid = ki.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🇲🇨 Group : "+str(len(gid))+"\n🇲🇨 Teman : "+str(len(teman))+"\n🇲🇨 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🇲🇨 Runtime : \n • "+bot
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ki.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@BotTroxᴮᴼᵀ "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭════════════════" + "\n" + \
                  "║»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» Help Message " + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "Cctv「on/off」\n" + \
				  "║»» " + key + "Creator\n" + \
				  "║»» " + key + "Cyduk\n" + \
				  "║»» " + key + "Help admin\n" + \
				  "║»» " + key + "Help blacklist\n" + \
				  "║»» " + key + "Help bot\n" + \
                  "║»» " + key + "Help creator\n" + \
				  "║»» " + key + "Help setting\n" + \
                  "║»» " + key + "Listbot\n" + \
                  "║»» " + key + "Listadmin\n" + \
				  "║»» " + key + "Status\n" + \
				  "║»══════════════" + "\n" + \
                  "║» http://line.me/ti/p/~iia008" + "\n" + \
                  "╰═══ CREATOR: ©Satria™"
    return helpMessage
    
    

def helpcreator():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭═════════════" + "\n" + \
                  "║»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱" + "\n" + \
                  "║»══════════════" + "\n" + \
                  "║»» Help CREATOR " + "\n" + \
                  "║»══════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "Refresh\n" + \
                  "║»» " + key + "Cek spam\n" + \
                  "║»» " + key + "Cek pesan\n" + \
                  "║»» " + key + "Cek respon\n" + \
                  "║»» " + key + "Cek welcome\n" + \
                  "║»» " + key + "Cek leave\n" + \
                  "║»» " + key + "Set spam:「Text」\n" + \
                  "║»» " + key + "Set pesan:「Text」\n" + \
                  "║»» " + key + "Set respon:「Text」\n" + \
                  "║»» " + key + "Set welcome:「Text」\n" + \
                  "║»» " + key + "Set leave:「Text」\n" + \
                  "║»» " + key + "Myname:「Name」\n" + \
                  "║»» " + key + "Bot1name:「Name」\n" + \
                  "║»» " + key + "Bot2name:「Name」\n" + \
                  "║»» " + key + "Botname:「Name」\n" + \
				  "║»» " + key + "Bot3name:「Name」\n" + \
                  "║»» " + key + "Satup「Foto」\n" + \
                  "║»» " + key + "Bot1up「Foto」\n" + \
                  "║»» " + key + "Bot2up「Foto」\n" + \
                  "║»» " + key + "Bot3up「Foto」\n" + \
				  "║»» " + key + "Bot4up「Foto」\n" + \
                  "║»» " + key + "Gift:「Mid」「Jumlah」\n" + \
                  "║»» " + key + "Spam:「Mid」「Jumlah」\n" + \
				  "║»» " + key + "Spamtag:「jumlahnya」\n" + \
                  "║»» " + key + "Spamtag「@」\n" + \
                  "║»» " + key + "Spamcall:「jumlahnya」\n" + \
                  "║»» " + key + "Spamcall\n" + \
                  "║»» " + key + "Broadcast:「Text」\n" + \
                  "║»» " + key + "Setkey「New Key」\n" + \
                  "║»» " + key + "Mykey\n" + \
                  "║»» " + key + "Resetkey\n" + \
				  "║»» " + key + "Bot「on/off」\n" + \
				  "║»» " + key + "Tag2\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»══ http://line.me/ti/p/~iia008" + "\n" + \
                  "╰══ CREATOR: ©Satria™"
    return helpMessage1

def helpblacklist():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╭══════════════" + "\n" + \
                  "║»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱" + "\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» Help Blacklist " + "\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "Banlist\n" + \
				  "║»» " + key + "Ban:on\n" + \
                  "║»» " + key + "Blc\n" + \
				  "║»» " + key + "Clearban\n" + \
				  "║»» " + key + "Refresh\n" + \
				  "║»» " + key + "Unban「@」\n" + \
				  "║»» " + key + "Unban:on\n" + \
				  "║»═══════════════" + "\n" + \
                  "║»══ http://line.me/ti/p/~iia008" + "\n" + \
                  "╰══ CREATOR: ©Satria™"
    return helpMessage3

def helpadmin():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "╭═══════════════" + "\n" + \
                  "║»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱" + "\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» Help Admin " + "\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "Me\n" + \
                  "║»» " + key + "Unsend [ on/off ]\n" + \
                  "║»» " + key + "Set\n" + \
                  "║»» " + key + "Mymid\n" + \
                  "║»» " + key + "Mid [ @ ]\n" + \
                  "║»» " + key + "Info [ @ ]\n" + \
                  "║»» " + key + "Creator\n" + \
                  "║»» " + key + "About\n" + \
                  "║»» " + key + "Contact admin\n" + \
                  "║»» " + key + "Contact staff\n" + \
                  "║»» " + key + "Sider:「on/off」\n" + \
                  "║»» " + key + "tag\n" + \
				  "║»» " + key + "Cctv [ on/off ]\n" + \
                  "║»» " + key + "Cyduk\n" + \
				  "║»» " + key + "Dor\n" + \
                  "║»» " + key + "Contact bot\n" + \
                  "║»» " + key + "Nk [ @ ]\n" + \
				  "║»» " + key + "Kick1 [ @ ]\n" + \
				  "║»» " + key + "Welcome on/off\n" + \
                  "║»» " + key + "Speed/Sp\n" + \
                  "║»» " + key + "Sprespon\n" + \
                  "║»» " + key + "Respon/Resp\n" + \
                  "║»» " + key + "Listadmin\n" + \
                  "║»» " + key + "Ginfo\n" + \
                  "║»════════════════" + "\n" + \
                  "║»══ http://line.me/ti/p/~iia008" + "\n" + \
                  "╰══ CREATOR: ©Satria™"
    return helpMessage4
    	
def helpsetting():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = "╭═══════════════" + "\n" + \
                  "║»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║» Help Setting " + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "Autoadd「on/off」\n" + \
				  "║»» " + key + "Autojoin「on/off」\n" + \
				  "║»» " + key + "Autoleave「on/off」\n" + \
				  "║»» " + key + "Contact「on/off」\n" + \
				  "║»» " + key + "Jointicket「on/off」\n" + \
				  "║»» " + key + "Respon「on/off」\n" + \
				  "║»» " + key + "Unsend「on/off」\n" + \
                  "║»» " + key + "Welcome「on/off」\n" + \
                  "║»═════════════════" + "\n" + \
                  "║»══ http://line.me/ti/p/~iia008" + "\n" + \
                  "╰══ CREATOR: ©Satria™"
    return helpMessage5
    
def helpprotect():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage6 = "╭════════════════" + "\n" + \
                  "║»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» Help Protect " + "\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
				  "║»» " + key + "Join all\n" + \
				  "║»» " + key + "Satpro 「on/off」\n" + \
                  "║»» " + key + "Notag「on/off」\n" + \
                  "║»» " + key + "Protecturl「on/off」\n" + \
                  "║»» " + key + "Protectjoin「on/off」\n" + \
                  "║»» " + key + "Protectkick「on/off」\n" + \
                  "║»» " + key + "Protectcancel「on/off」\n" + \
                  "║»» " + key + "Protectinvite「on/off」\n" + \
				  "║»════════════════" + "\n" + \
                  "║»══ http://line.me/ti/p/~iia008" + "\n" + \
                  "╰══ CREATOR: ©Satria™"
    return helpMessage6
	
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage8 = "╭════════════════" + "\n" + \
                  "║»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» Help BOT" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "About\n" + \
				  "║»» " + key + "Close\n" + \
				  "║»» " + key + "Ginfo\n" + \
				  "║»» " + key + "Gruplist\n" + \
				  "║»» " + key + "Info 「@」\n" + \
				  "║»» " + key + "「@」Kick\n" + \
				  "║»» " + key + "Me\n" + \
                  "║»» " + key + "Mid「@」\n" + \
				  "║»» " + key + "Mybot\n" + \
                  "║»» " + key + "Mymid\n" + \
				  "║»» " + key + "Open\n" + \
				  "║»» " + key + "Respon\n" + \
				  "║»» " + key + "Restart\n" + \
				  "║»» " + key + "Runtime\n" + \
				  "║»» " + key + "Speed/Sp\n" + \
                  "║»» " + key + "Sprespon\n" + \
				  "║»» " + key + "Stealname「@」\n" + \
                  "║»» " + key + "Stealbio「@」\n" + \
                  "║»» " + key + "Stealcover「@」\n" + \
				  "║»» " + key + "Stealpicture「@」\n" + \
                  "║»» " + key + "Stealvideoprofile「@」\n" + \
                  "║»» " + key + "___________\n" + \
                  "║»════════════════" + "\n" + \
                  "║»══ http://line.me/ti/p/~iia008" + "\n" + \
                  "╰═════ CREATOR: ©Satria™"
    return helpMessage8

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if random.choice(KAC).getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
                            random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                            wait["blacklist"][op.param2] = True
                except:
                            G.preventedJoinByTicket = True
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            wait["blacklist"][op.param2] = True
                else:
                    pass  
        
        if op.type == 11:
            if wait["qr"] == True:
                try:
                    if random.choice(ABC).getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            random.choice(ABC).reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            random.choice(ABC).updateGroup(X)
                            random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass  
                    
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Hai " + str(ginfo.name))                        
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"Hai " + str(ginfo.name))                        
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        kg.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kg.leaveGroup(op.param1)
                    else:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        kg.sendMessage(op.param1,"Hai " + str(ginfo.name))        
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        kh.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kh.leaveGroup(op.param1)
                    else:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        kh.sendMessage(op.param1,"Hai " + str(ginfo.name))                                                                

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = random.choice(KAC).getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 13:
            if wait["proinvite"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = random.choice(ABC).getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = ki.getGroup(op.param1)
                contact = ki.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                ki.sendImageWithURL(op.param1, image)

      #  if op.type == 17:
          #  if op.param1 in protectjoin:
              #  if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
               #     wait["blacklist"][op.param2] = True
                #    try:
                    #    if op.param3 not in wait["blacklist"]:
                      #  	kf.kickoutFromGroup(op.param1,[op.param2])
               #     except:
                    #    try:
                       #     if op.param3 not in wait["blacklist"]:
                           #     ke.kickoutFromGroup(op.param1,[op.param2])
                    #    except:
                        #    try:
                         #       if op.param3 not in wait["blacklist"]:
                               #     kd.kickoutFromGroup(op.param1,[op.param2])
                        #    except:
                            #    try:
                                #    if op.param3 not in wait["blacklist"]:
                                #        kb.kickoutFromGroup(op.param1,[op.param2])
                             #   except:
                                 #   try:
                                    #    if op.param3 not in wait["blacklist"]:
                                        #    kc.kickoutFromGroup(op.param1,[op.param2]) 
                                  #  except:
                                     #   try:
                                           # if op.param3 not in wait["blacklist"]:
                                         #       kk.kickoutFromGroup(op.param1,[op.param2]) 
                                   #     except:
                                      #     try:
                                             #  if op.param3 not in wait["blacklist"]:
                                          #         ki.kickoutFromGroup(op.param1,[op.param2]) 
                                        #   except:
                                            #  try:
                                             #     if op.param3 not in wait["blacklist"]:
                                              #        cl.kickoutFromGroup(op.param1,[op.param2])                                        
                                          #    except:
                                         #         pass
                          #      return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        ki.sendText(op.param1, wait["message"])

#============ Protect Kick ============  
       # elif op.type == 19: #Admin Ke Kick
                elif op.param2 in admin:
                    if op.param2 in Bots:
                     pass
            else:
                try:
                  kicked = ki.getContact(op.param3).mid
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  ki.findAndAddContactsByMid(kicked)
                  ki.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  kicked = random.choice(KAC).getContact(op.param3).mid
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(kicked)
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True                           
                  
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        satria.acceptGroupInvitationByTicket(op.param1,Ticket)
                        satria.kickoutFromGroup(op.param1,[op.param2])
                        satria.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
                
        if op.type == 32:
            if op.param3 in Zmid:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)                                     
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    X = kh.getGroup(op.param1)
                    kh.updateGroup(X)
                    X.preventedJoinByTicket = True
                    kh.inviteIntoGroup(op.param1,[Zmid])
                    wait["blacklist"][op.param2] = True
                else:
                    pass

        if op.type == 32:
            if op.param3 in Hmid:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)                                     
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    X = kh.getGroup(op.param1)
                    kh.updateGroup(X)
                    X.preventedJoinByTicket = True
                    kh.inviteIntoGroup(op.param1,[Hmid])
                    wait["blacklist"][op.param2] = True
                else:
                    pass
#-------------------------------------------------------------------------------                        
        #if op.type == 19:
          #  if op.param1 in protectkick:
             #   if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  #  wait["blacklist"][op.param2] = True
                  #  random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
               # else:
                   # pass             

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                     # random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True

        if op.type == 32:
            if wait["cancell"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                     # random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                      #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                     # random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                      
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.kickoutFromGroup(op.param1,[op.param2])                                    
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            kd.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                ke.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                            ke.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                                kf.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kd.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kd.updateGroup(G)
                                    Ticket = kd.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    G = kd.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kd.updateGroup(G)
                                    Ticket = kd.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kf.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                            kf.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kh.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                                kh.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                            kd.acceptGroupInvitation(op.param1)
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kg.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                            kg.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kh.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                                kh.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kf.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kf.updateGroup(G)
                                    Ticket = kf.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    G = kf.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kf.updateGroup(G)
                                    Ticket = kf.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kg.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kh.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                            kh.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kg.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kg.updateGroup(G)
                                    Ticket = kg.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                    G = kg.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kg.updateGroup(G)
                                    Ticket = kg.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)
                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                            kf.acceptGroupInvitation(op.param1)
                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kh.inviteIntoGroup(op.param1,[op.param3])
                        kg.acceptGroupInvitation(op.param1)
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kg.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kg.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kh.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kh.updateGroup(G)
                                    Ticket = kh.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.kickoutFromGroup(op.param1,[op.param2])
                                    G = kh.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kh.updateGroup(G)
                                    Ticket = kh.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                        kg.acceptGroupInvitation(op.param1)
                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kg.acceptGroupInvitation(op.param1)
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kh.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kh.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kh.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kh.acceptGroupInvitation(op.param1)
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            kh.acceptGroupInvitation(op.param1)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
                
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["readPoint"]:
                   if op.param2 in Setmain["readMember"][op.param1]:
                       pass
                   else:
                       Setmain["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = ki.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = ki.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        ki.sendImageWithURL(op.param1, image)                        
                        
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = ki.getGroup(at)
                                Satria = ki.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "⏩Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n⏩Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Satria.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Satria.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                ki.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                ki.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = ki.getGroup(at)
                                Satria = ki.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "⏩Pengirim : {}".format(str(Satria.displayName))
                                ret_ += "\n⏩Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n⏩Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n⏩Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ki.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = ki.getGroup(at)
                                Satria = ki.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "⏩Pengirim : {}".format(str(Satria.displayName))
                                ret_ += "\n⏩Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n⏩Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                ki.sendMessage(at, str(ret_))
                                ki.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)        
                                                                                                                                                                                                                                                                                                                                           
        if op.type == 26 or op.type == 25:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           ki.sendMessage(msg.to, wait["Respontag"])
                           ki.sendMessage(msg.to, None, contentMetadata={"STKID":"52114126","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           ki.sendMessage(msg.to, "Ye ngetag ngetag, lu minta digift ya? cek PersonalChat bos, udah gue gift tuh. Jangan lupa bilang makasih yak!")
                           ki.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           ki.sendMessage(msg.to, "Jangan tag saya....")
                           ki.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    ki.sendMessage(msg.to,"「Cek ID Sticker」\n🇲🇨 STKID : " + msg.contentMetadata["STKID"] + "\n🇲🇨 STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🇲🇨 STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    ki.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        path = ki.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        ki.sendMessage(msg.to,"⏩ Nama: " + msg.contentMetadata["displayName"] + "\n⏩ MID: " + msg.contentMetadata["mid"] + "\n⏩ Status: " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        ki.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = ki.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n⏩Sticker ID : {}".format(stk_id)
                   ret_ += "\n⏩Sticker Version : {}".format(stk_ver)
                   ret_ += "\⏩Sticker Package : {}".format(pkg_id)
                   ret_ += "\n⏩Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = ki.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
                    if msg.contentType == 16:
                        if wait["Shared"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = ki.getContact(msg.contentMetadata[op.param3])
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://me.me/R/"))
                               # ki.likePost(purl[25:58], purl[66:], likeType=1001)
                                #ki.sendMessage(purl[25:58], purl[66:], wait["comment"])
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://me.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                ki.sendMessage(to, str(ret_))
                            except Exception as error:
                               print (error)
                                #traceback.print_tb(error.__traceback__)
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    ki.sendMessage(msg.to,"⏩STKID : " + msg.contentMetadata["STKID"] + "\n⏩STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n⏩STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    ki.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        path = ki.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        ki.sendMessage(msg.to,"⏩Nama : " + msg.contentMetadata["displayName"] + "\n⏩MID : " + msg.contentMetadata["mid"] + "\n⏩Status Msg : " + contact.statusMessage + "\n⏩Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        ki.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = ki.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            ki.sendMessage(msg.to, "Maaf, dia ada di daftar blacklist\n")
                            break
                        else:
                            targets.append(invite["mid"])
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  ki.findAndAddContactsByMid(targetUserIds)
                                  ki.inviteIntoGroup(msg.to,[target])
                                  ryan = ki.getContact(targetUserIds)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "Ketik invite off jika sudah masuk"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  ki.sendReplyMessage(msg.id,msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  ki.sendMessage(msg.to,"ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʟɪᴍɪᴛ")
                                  wait["invite"] = False
                                  break
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        ki.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        kk.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        kc.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        kb.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        kd.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        ke.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        kf.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        kh.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        ki.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        kk.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        kc.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        kb.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        kd.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        ke.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        kf.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        kg.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                        kh.sendMessage(msg.to,"Berhasil menambahkan anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        ki.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        kk.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        kc.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        kb.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        kd.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        ke.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        kf.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        kg.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                        kh.sendMessage(msg.to,"Berhasil menghapus anggota bot")
                    else:
                        wait["dellbots"] = True
                        ki.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        kk.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        kc.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        kb.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        kd.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        ke.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        kf.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        kg.sendMessage(msg.to,"Contact itu bukan anggota bot")
                        kh.sendMessage(msg.to,"Contact itu bukan anggota bot")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        ki.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        kk.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        kc.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        kb.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        kd.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        ke.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        kf.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        kg.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        kh.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        ki.sendMessage(msg.to,"Berhasil menambahkan staff")
                        kk.sendMessage(msg.to,"Berhasil menambahkan staff")
                        kc.sendMessage(msg.to,"Berhasil menambahkan staff")
                        kb.sendMessage(msg.to,"Berhasil menambahkan staff")
                        kd.sendMessage(msg.to,"Berhasil menambahkan staff")
                        ke.sendMessage(msg.to,"Berhasil menambahkan staff")
                        kf.sendMessage(msg.to,"Berhasil menambahkan staff")
                        kg.sendMessage(msg.to,"Berhasil menambahkan staff")
                        kh.sendMessage(msg.to,"Berhasil menambahkan staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        ki.sendMessage(msg.to,"Berhasil menghapus staff")
                        kk.sendMessage(msg.to,"Berhasil menghapus staff")
                        kc.sendMessage(msg.to,"Berhasil menghapus staff")
                        kb.sendMessage(msg.to,"Berhasil menghapus staff")
                        kd.sendMessage(msg.to,"Berhasil menghapus staff")
                        ke.sendMessage(msg.to,"Berhasil menghapus staff")
                        kf.sendMessage(msg.to,"Berhasil menghapus staff")
                        kg.sendMessage(msg.to,"Berhasil menghapus staff")
                        kh.sendMessage(msg.to,"Berhasil menghapus staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        ki.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        ki.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        ki.sendMessage(msg.to,"Berhasil menambahkan admin")
                        kk.sendMessage(msg.to,"Berhasil menambahkan admin")
                        kc.sendMessage(msg.to,"Berhasil menambahkan admin")
                        kb.sendMessage(msg.to,"Berhasil menambahkan admin")
                        kd.sendMessage(msg.to,"Berhasil menambahkan admin")
                        ke.sendMessage(msg.to,"Berhasil menambahkan admin")
                        kf.sendMessage(msg.to,"Berhasil menambahkan admin")
                        kg.sendMessage(msg.to,"Berhasil menambahkan admin")
                        kh.sendMessage(msg.to,"Berhasil menambahkan admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        ki.sendMessage(msg.to,"Berhasil menghapus admin")
                        kk.sendMessage(msg.to,"Berhasil menghapus admin")
                        kc.sendMessage(msg.to,"Berhasil menghapus admin")
                        kb.sendMessage(msg.to,"Berhasil menghapus admin")
                        kd.sendMessage(msg.to,"Berhasil menghapus admin")
                        ke.sendMessage(msg.to,"Berhasil menghapus admin")
                        kf.sendMessage(msg.to,"Berhasil menghapus admin")
                        kg.sendMessage(msg.to,"Berhasil menghapus admin")
                        kh.sendMessage(msg.to,"Berhasil menghapus admin")
                    else:
                        wait["delladmin"] = True
                        ki.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ki.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        ki.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        kk.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        kc.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        kb.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        kd.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        ke.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        kf.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        kg.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                        kh.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        kk.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        kc.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        kb.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        kd.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        ke.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        kf.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        kg.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                        kh.sendMessage(msg.to,"Berhasil menghapus blacklist user")
                    else:
                        wait["dblacklist"] = True
                        ki.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        ki.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        ki.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        ki.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        ki.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = ki.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            ki.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = ki.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     ki.updateGroupPicture(msg.to, path)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["foto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["foto"][mid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["foto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["foto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["foto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        ki.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()                         
                               veza = ki.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭──────────────────╮\n│✮BotTroxᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ : "
                               ret_ = str(helpMessage)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               ki.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                                                                       
                        if cmd == "bot on":
                            if msg._from in creator:
                                wait["selfbot"] = True
                                ki.sendMessage(msg.to, "Bot diaktifkan")
                                
                        elif cmd == "bot off":
                            if msg._from in creator:
                                wait["selfbot"] = False
                                ki.sendMessage(msg.to, "Bot dinonaktifkan")
                                            
                        elif cmd == "help creator":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpcreator()
                               veza = ki.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭──────────────────╮\n│✮BotTroxᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ : "
                               ret_ = str(helpMessage1)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               ki.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "help admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpadmin()
                               veza = ki.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭──────────────────╮\n│✮BotTroxᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ : "
                               ret_ = str(helpMessage4)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               ki.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                               
                        elif cmd == "help setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage5 = helpsetting()
                               veza = ki.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭──────────────────╮\n│✮BotTroxᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ : "
                               ret_ = str(helpMessage5)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               ki.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)                      

                        elif cmd == "help protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage6 = helpprotect()
                               veza = ki.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭──────────────────╮\n│✮BotTroxᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ : "
                               ret_ = str(helpMessage6)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               ki.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage8 = helpbot()
                               veza = ki.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭──────────────────╮\n│✮BotTroxᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ : "
                               ret_ = str(helpMessage8)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               ki.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "help blacklist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpblacklist()
                               veza = ki.getContact(mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan =  "╭──────────────────╮\n│✮BotTroxᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ : "
                               ret_ = str(helpMessage3)
                               ry = str(veza.displayName)
                               pesan = ''
                               pesan2 = pesan+"@x \n\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan + zxc + ret_ + ""
                               ki.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                ki.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                ki.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭═ ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ ═\n║»».        STATUS BOTS\n"
                                if wait["unsend"] == True: md+="║»» ✔️ Unsend「ON」\n"
                                else: md+="║»» ❌ Unsend「OFF」\n"          
                                if wait["sticker"] == True: md+="║»» ✔️Sticker「ON」\n"
                                else: md+="║»» ❌Sticker [ Off ]\n"
                                if wait["contact"] == True: md+="║»» ✔️Contact「ON」\n"
                                else: md+="║»» ❌Contact「OFF」\n"
                                if wait["talkban"] == True: md+="║»» ✔️Talkban「ON」\n"
                                else: md+="║»» ❌Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="║»» ✔️Notag「ON」\n"
                                else: md+="║»» ❌Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="║»» ✔️Respon「ON」\n"
                                else: md+="║»» ❌Respon「OFF」\n"
                                if wait["autoJoin"] == True: md+="║»» ✔️Autojoin「ON」\n"
                                else: md+="║»» ❌Autojoin「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="║»» ✔️Jointicket「ON」\n"
                                else: md+="║»» ❌Jointicket「OFF」\n"  
                                if wait["autoAdd"] == True: md+="║»» ✔️Autoadd「ON」\n"
                                else: md+="║»» ❌Autoadd「OFF」\n"
                                if msg.to in welcome: md+="║»» ✔️Welcome「ON」\n"
                                else: md+="║»» ❌Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="║»» ✔️Autoleave「ON」\n"
                                else: md+="║»» ❌Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="║»» ✔️Protecturl「ON」\n"
                                else: md+="║»» ❌Protecturl「OFF」\n"
                                if msg.to in protectinvite: md+="║»» ✔️ Protectinvite「ON」\n"
                                else: md+="║»» ❌Protectinvite「OFF」\n" 
                                if msg.to in protectkick: md+="║»» ✔️Protectkick「ON」\n"
                                else: md+="║»» ❌Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="║»» ✔️Protectcancel「ON」\n"
                                else: md+="║»» ❌Protectcancel「OFF」\n"
                                if msg.to in protectantijs: md+="║»» ✔️Antijs「ON」\n"
                                else: md+="║»» ❌Antijs「OFF」\n"  
                                if msg.to in ghost: md+="║»» ✔️Ghost「ON」\n"
                                else: md+="║»» ❌Ghost「OFF」\n"                                   
                                ginfo = ki.getGroup(msg.to)
                                ryan = ki.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭──────────────────╮\n│「 sᴇᴛ user」\n│♠ Creator: "
                                ret_ = "│♠ ɢʀᴏᴜᴘ: {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "┝────────────────\n│♠ ᴄʟᴏᴄᴋ: 「"+ datetime.strftime(timeNow,'%H:%M:%S')+"」 "+"\n│♠ BotTroxᴮᴼᵀ ᴅᴀᴛᴇ: 「"+ datetime.strftime(timeNow,'%Y-%m-%d') +"」\n╰────BotTroxᴮᴼᵀஜ─────╯"
                                ki.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                ki.sendMessage(msg.to,"Creator Bot") 
                                ma = ""
                                for i in creator:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "About":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ 」\n")
                               ki.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'mek':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.sendContact(to, sender)
                               sendMention2(to, "╭────ஜ۩BotTroxᴮᴼᵀ۩ஜ─────╮\n│✆「sᴇʟғ ᴠ.0.11.0」 \n│✆「ᴛʏᴘᴇ BotTroxᴮᴼᵀ」 \n│✆「ᴄᴏᴍᴇ ᴏɴ ᴏʀᴅᴇʀ」 \n│✆「ᴡᴇ ᴀʀᴇ BotTroxᴮᴼᵀ」\n│✆「ᴜsᴇʀ: @! 」\n╰────ஜ۩BotTroxᴮᴼᵀ۩ஜ─────╯",[sender])
                               
                        elif text.lower() == "aku":
                            if msg._from in creator:                        	
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                             hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                             bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                             hr = timeNow.strftime("%A")
                             bln = timeNow.strftime("%m")
                             for i in range(len(day)):
                                 if hr == day[i]: hasil = hari[i]
                             for k in range(0, len(bulan)):
                                 if bln == str(k): bln = bulan[k-1]
                             readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                             cl.sendMessage(to,"┣━━╦KONTAK PROFILE╦━━╣\n " + readTime)
                             sendMeention(to, "@!", [sender])
                             cl.sendContact(to, sender)                     

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               ki.sendMessage(msg.to, msg._from)
                        elif text.lower() == 'salam':
                               ki.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'assalamualaikum':
                               ki.sendMessage(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif text.lower() == 'waalaikumsalam':
                               ki.sendMessage(msg.to, "ُиαн gιтυ ∂σик кαк.. кαℓαυ α∂α уαиg ѕαℓαм ∂ι ʝαωαв.. тєяιмα кαѕιн кαк")
                               
                        elif text.lower() == "allmid":
                            if msg._from in admin:
                               h = cl.getContact(mid)
                               cl.sendMessage(to,h.mid)
                               h = ki.getContact(Amid)
                               ki.sendMessage(to, h.mid)
                               h = kk.getContact(Bmid)
                               kk.sendMessage(to, h.mid)
                               h = kc.getContact(Cmid)
                               kc.sendMessage(to, h.mid)
                               h = kb.getContact(Dmid)
                               kb.sendMessage(to, h.mid)
                               h = kd.getContact(Emid)
                               ki.sendMessage(to, h.mid)
                               h = ke.getContact(Fmid)
                               ke.sendMessage(to, h.mid)
                               h = kf.getContact(Gmid)
                               kf.sendMessage(to, h.mid)
                               h = kg.getContact(Imid)
                               kg.sendMessage(to, h.mid)
                               h = kh.getContact(Jmid)
                               kh.sendMessage(to, h.mid)
                               h = satria.getContact(Hmid)
                               satria.sendMessage(to, h.mid)
                               h = sw.getContact(Zmid)
                               sw.sendMessage(to, h.mid)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = ki.getContact(key1)
                               ki.sendMessage(msg.to, "╔──────────────────╗\n│🌍ɴᴀᴍᴇ: "+str(mi.displayName)+"\n│🌍ᴍɪᴅ: " +key1+ "\n╚────ஜ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ஜ─────╝")
                               ki.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = ki.getContact(key1)
                               ki.sendMessage(msg.to, "╔──────────────────╗\n│🌍ɴᴀᴍᴇ: "+str(mi.displayName)+"\n│🌍ᴍɪᴅ: " +key1+"\n│🌍sᴛᴀᴛᴜs"+str(mi.statusMessage)+"\n╚────ஜ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ஜ─────╝")
                               ki.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(ki.getContact(key1)):
                                   ki.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   ki.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   kh.removeAllMessages(op.param2)
                                   satria.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("stealname "):
                          if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = ki.getContact(ls)
                                      ki.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            
                        elif cmd.startswith("stealbio "):
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = ki.getContact(ls)
                                      ki.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            
                        elif cmd.startswith("stealpicture "):
                            if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line-cdn.net/" + ki.getContact(ls).pictureStatus
                                        ki.sendImageWithURL(msg.to, str(path))
                            
                        elif cmd.startswith("stealcover "):
                            if msg._from in admin:
                                if line != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = ki.getProfileCoverURL(ls)
                                            ki.sendImageWithURL(msg.to, str(path))
                        elif cmd.startswith("stealvideoprofile "):
                            if msg._from in admin:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            contact = ki.getContact(target)
                                            path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                            ki.sendVideoWithURL(msg.to, path)
                                        except Exception as e:
                                            pass                                            

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = ki.getGroupIdsJoined()
                               for group in saya:
                                   ki.sendMessage(group,"[ Broadcast ]\n" + responsename0 + str(pesan))
                                   
                        elif cmd.startswith("gb: "):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                bctxt = cmd.replace("gb: ", "")
                                a = ki.getGroupIdsJoined()
                                me = ki.getProfile()
                                name = "ʙʀᴏᴀᴅᴄᴀsᴛ ɢʀᴏᴜᴘ"
                                url = 'https://line.me/ti/p/{}'.format(str(cl.getUserTicket().id))
                                iconlink = "http://dl.profile.line-cdn.net/{}".format(str(me.pictureStatus))
                                ki.sendMessage(to, "sᴜᴄᴄᴇss ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴ: "+str(len(a))+" ɢʀᴏᴜᴘ")
                                for manusia in a:
                                    C = ki.getContact(mid)
                                    mids = [C.mid]
                                    text = "{}\n「BotTrox ʙᴄ」\nBotTrox : @!".format(str(bctxt))
                                    sendMentionV2(manusia, text, mids,str(name),str(url),str(iconlink))
                                    
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   ki.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   ki.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               Setmain["keyCommand"] = ""
                               ki.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "Restart Sukses Bos!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               ki.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = ki.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ki.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ki.sendMessage(msg.to, "║»» BOT Grup Info\n\n ║»» Nama Group : {}".format(G.name)+ "\n»» ID Group : {}".format(G.id)+ "\n»» Pembuat : {}".format(G.creator.displayName)+ "\n»» Waktu Dibuat : {}".format(str(timeCreated))+ "\n»» Jumlah Member : {}".format(str(len(G.members)))+ "\n»» Jumlah Pending : {}".format(gPending)+ "\n»» Group Qr : {}".format(gQr)+ "\n»» Group Ticket : {}".format(gTicket))
                                ki.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                ki.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                ki.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = ki.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "❧⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱ Fams Grup Info\n"
                                ret_ += "\n❧Nama Group : {}".format(G.name)
                                ret_ += "\n❧ID Group : {}".format(G.id)
                                ret_ += "\n❧Pembuat : {}".format(gCreator)
                                ret_ += "\n❧Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n❧Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n❧Jumlah Pending : {}".format(gPending)
                                ret_ += "\n❧Group Qr : {}".format(gQr)
                                ret_ += "\n❧Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"ɢʀᴏᴜᴘ ɴᴀᴍᴇ: [ " + str(G.name) + " ]\n\n   [ ʟɪsᴛ ᴍᴇᴍʙᴇʀ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
                               
                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "║»» " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to, responsename0 + "╭════════[ GROUP LIST ]\n║»»\n"+ma+"║»»\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "║»» " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n║»»\n"+ma+"║»»\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "║»» " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n║»»\n"+ma+"║»»\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "║»» " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n║»»\n"+ma+"║»»\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "QR telah dibuka")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "QR telah ditutup")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                if msg.toType == 2:
                                   x = ki.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ki.updateGroup(x)
                                   gurl = ki.reissueGroupTicket(msg.to)
                                   ki.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                        elif 'like ' in text.lower():
                           if msg._from in admin:
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = ki.getContact(u).mid
                                    s = ki.getContact(u).displayName
                                    hasil = ki.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        #ki.likePost(str(msg.to), str(result), likeType=random.choice(typel))
                                        ki.createComment(str(msg.to), str(result), wait["comment"])
                                    ki.sendMessage(msg.to, 'ɢʜᴅ ᴅᴏɴᴇ ʟɪᴋᴇ ᴀɴᴅ ᴄᴏᴍᴍᴇɴᴛ '+str(len(st))+' ᴘᴏsᴛ ғʀᴏᴍ' + str(s))
                                except Exception as e:
                                    ki.sendMessage(msg.to, str(e))
#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "satup":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                Setmain["foto"][mid] = True
                                cl.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in creator:
                                Setmain["foto"][Amid] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in creator:
                                Setmain["foto"][Bmid] = True
                                kk.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in creator:
                                Setmain["foto"][Cmid] = True
                                kc.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in creator:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in creator:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in creator:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in creator:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tag" or text.lower() == 'dor':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	group = ki.getGroup(msg.to)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = ".       ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱  \n╔════════════\n   MENTION USER \n╚════════════\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠[{}] @!".format(str(no))
                                  ret_ += "\n╚══════════════\n╔═══════════════\n.  TOTAL MEMBER [ {} ]\n╚═══════════════\n.        ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱\n╰══ CREATOR: ©Satria \nhttps://line.me/ti/p/~iia008".format(str(len(dataMid))) 
                                  sendMeention2(msg.to, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe) 

                        elif cmd == "biji" or text.lower() == '🤔':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                            	group = cl.getGroup(msg.to)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers2 in range(Dmem+1):                               
                                  no = 0 
                                #  ret_ = "[ @! ]\n"
                                  ret_ = "       ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱  \n╔════════════\n   MENTION USER \n╚════════════\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers2*20 : (mentionMembers2+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠[{}] @!".format(str(no))
                                  ret_ += "\n╚══════════════\n╔═══════════════\n.  TOTAL MEMBER [ {} ]\n╚═══════════════\n.        ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱\n╰══ CREATOR: ©Satria \nhttps://line.me/ti/p/~iia008".format(str(len(dataMid)))      
                                  sendMeention(msg.to, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe) 
                              
                        elif cmd == 'haii':
                         #if wait["selfbot"] == True:
                         if msg._from in creator:
                            members = []
                            if msg.toType == 1:
                               room = cl.getRoom(to)
                               members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                               group = cl.getGroup(to)
                               members = [mem.mid for mem in group.members]
                            else:
                               return cl.sendReplyMessage(msg_id, to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                               mentionMembers1(to, members)
                               
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +ki.getContact(m_id).displayName + "\n"
                                ki.sendMessage(msg.to,"»» BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "adminlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +ki.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +ki.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +ki.getContact(m_id).displayName + "\n"
                                ki.sendMessage(msg.to,"»»       ADMIN \n⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱\n\nOwner :\n"+ma+"\nAdmin :\n"+mb+"\nStaff :\n"+mc+"\nTotal「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +ki.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +ki.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +ki.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +ki.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +ki.getGroup(group).name + "\n"                                    
                                ki.sendMessage(msg.to,"»» ⊰์◉⊱B❂TTR❂X B❂T$⊰์◉⊱\n.     PROTECT\n\n»» PROTECT URL :\n"+ma+"\n»» PROTECT KICK :\n"+mb+"\n»» PROTECT JOIN :\n"+md+"\n»» PROTECT CANCEL:\n"+mc+"\n»» PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "resp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            #	cl.sendMessage(msg.to,responsename0)
                                ki.sendMessage(msg.to,responsename1+ '\nBOTS 1 HADIR BOSS!!')
                                kk.sendMessage(msg.to,responsename2+ '\nBOTS 2 HADIR BOSS!!')
                                kc.sendMessage(msg.to,responsename3+ '\nBOTS 3 HADIR BOSS!!')
                                kb.sendMessage(msg.to,responsename4+ '\nBOTS 4 HADIR BOSS!!')
                                kd.sendMessage(msg.to,responsename5+ '\nBOTS 5 HADIR BOSS!!')
                                ke.sendMessage(msg.to,responsename6+ '\nBOTS 6 HADIR BOSS!!')
                                kf.sendMessage(msg.to,responsename7+ '\nBOTS 7 HADIR BOSS!!')
                                kg.sendMessage(msg.to,responsename8+ '\nBOTS 8 HADIR BOSS!!')
                                kh.sendMessage(msg.to,responsename9+ '\nBOTS 9 HADIR BOSS!!')
                               # satria.sendMessage(msg.to,responsename10)
                                #sw.sendMessage(msg.to,responsename11)
                                cl.sendMessage(msg.to,responsename0+ '\nSEMUA BOTS HADIR BOSS!!')
                                
                        elif cmd == "ghost respon" or text.lower() == 'ghost resp':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               satria.sendMessage(msg.to,responsename10 + '\nGHOST HADIR BOSS!!')

                        elif cmd == "antijs respon" or text.lower() == 'antijs resp':
                          if wait["selfbot"] == True:
                            if msg._from in admin:       
                               sw.sendMessage(msg.to,responsename11+'\nANTIJS HADIR BOSS!!')
                               
                        elif cmd == "1assistinvite":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    anggota = [Amid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "botinvite":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    anggota = [Jmid,Imid,Gmid,Fmid,Emid,Dmid,Cmid,Bmid,Amid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    kh.acceptGroupInvitation(msg.to)
                                    kg.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                except:
                                    pass
 
                        elif cmd == "assist1":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)       
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                    
                        elif cmd == "bot2invite":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    anggota = [Hmid,Zmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    satria.acceptGroupInvitation(msg.to)
                                    sw.acceptGroupInvitation(msg.to)
                                except:
                                    pass                                    
                                
                        elif cmd == "antijs stay":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass                                
    
                        elif cmd == "join all":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                satria.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kh.updateGroup(G)

                        elif cmd == "bye bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Bye group "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)

                        elif cmd == "bye all":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                            	#G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Bye!!")
                                kk.sendMessage(msg.to, "Bye!!")
                                kc.sendMessage(msg.to, "Bye!!")
                                kb.sendMessage(msg.to, "Bye!!")
                                kd.sendMessage(msg.to, "Bye!!")
                                ke.sendMessage(msg.to, "Bye!!")
                                kf.sendMessage(msg.to, "Bye!!")
                                kg.sendMessage(msg.to, "Bye!!")
                                kh.sendMessage(msg.to, "Bye!!")
                                satria.sendMessage(msg.to, "Bye!!")
                                sw.sendMessage(msg.to, "Bye!!")
                              #  cl.sendMessage(msg.to, "Bye all")
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                                satria.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                               # cl.leaveGroup(msg.to)

                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        kf.leaveGroup(i)
                                        kg.leaveGroup(i)
                                        kh.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)
                                
                        elif cmd == "kicker join":
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)
                              
                        elif cmd == "ghost join":
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                satria.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = satria.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                satria.updateGroup(G)  
                                
                        elif cmd == "kicker bye":
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "ghost bye":
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                satria.leaveGroup(msg.to)                                

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = ki.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = ki.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = ki.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                ki.sendMessage(msg.to, " »» Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/1000,get_contact_time/1000,get_group_time/1000))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention1(msg.to, sender, "⏩sᴘᴇᴇᴅ ᴜᴘ\n⏩ᴜsᴇʀ:","")
                               start = time.time() 
                               time.sleep(0.0002)  
                               elapsed_time = time.time() - start
                               ki.sendMessage(msg.to,format(str(elapsed_time)))
                               kk.sendMessage(msg.to,format(str(elapsed_time)))
                               kc.sendMessage(msg.to,format(str(elapsed_time)))
                               kb.sendMessage(msg.to,format(str(elapsed_time)))
                               kd.sendMessage(msg.to,format(str(elapsed_time)))
                               kf.sendMessage(msg.to,format(str(elapsed_time)))
                               kg.sendMessage(msg.to,format(str(elapsed_time)))
                               kh.sendMessage(msg.to,format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['readPoint'][msg.to] = msg_id
                                 Setmain['readMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['readPoint'][msg.to]
                                 del Setmain['readMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['readPoint']:
                                if Setmain['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['readPoint'][msg.to]
                                        del Setmain['readMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['readPoint'][msg.to] = msg.id
                                    Setmain['readMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider:on":
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  ki.sendMessage(msg.to, "╔═══════════════\n╠ Cek sider diaktifkan\n╠═══════════════\n╠ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╚═══════════════")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider:off":
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  ki.sendMessage(msg.to, "╔═══════════════\n╠ Cek sider dinonaktifkan\n╠═══════════════\n╠ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╚═══════════════")
                              else:
                                  ki.sendMessage(msg.to, "Sudak tidak aktif")     
  
                        elif cmd.startswith("musik "):
                            query = msg.text.replace("musik","")
                            search = query.replace(" ","+")
                            result = requests.get("https://api.zicor.ooo/joox.php?song={}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            ret_ = "-•••>> Play Music <<•••-"
                            ret_ += "\n- Judul : {}".format(data["title"])
                            ret_ += "\n- Artis : {}".format(data["singer"])
                            ret_ += "\n- Lirik :\n{}".format(data["lyric"])
                            ki.sendImageWithURL(to, data["image"])
                            #cl.sendMessage(msg_id, to, ret_)
                            ki.sendAudioWithURL(to, data["url"])         
              
                        elif cmd.startswith("invite: "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = ki.findContactsByUserid(idnya)
                               ki.findAndAddContactsByMid(conn.mid)
                               ki.inviteIntoGroup(msg.to,[conn.mid])
                               group = ki.getGroup(msg.to)
                               xname = ki.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               ki.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                               
                        elif msg.text.lower().startswith("smule: "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            ki.sendMessage(to, "ini id smulenya kak\n" + smule)
                            ki.sendImageWithURL(msg.to, smule)
                       
                        elif cmd.startswith("lucu"):
                          if wait["selfbot"] == True:
                           if msg._from in admin:  
                                cl.sendMessage(to, None, contentMetadata={"STKID":"2713768","STKPKGID":"3524","STKVER":"1"}, contentType=7)
                                
                        elif cmd.startswith("tidur"):
                          if wait["selfbot"] == True:
                           if msg._from in admin:  
                                cl.sendMessage(to, None, contentMetadata={"STKID":"14870181","STKPKGID":"1380118","STKVER":"1"}, contentType=7)    
                                cl.sendMessage(to, None, contentMetadata={"STKID":"8970815","STKPKGID":"1220947","STKVER":"1"}, contentType=7)    
                                
                        elif cmd.startswith("ups"):
                          if wait["selfbot"] == True:
                           if msg._from in admin:  
                                cl.sendMessage(to, None, contentMetadata={"STKID":"8970787","STKPKGID":"1220947","STKVER":"1"}, contentType=7)                                    

                        elif cmd.startswith("pusing"):
                          if wait["selfbot"] == True:
                           if msg._from in admin:  
                                cl.sendMessage(to, None, contentMetadata={"STKID":"89547154","STKPKGID":"4834339","STKVER":"1"}, contentType=7) 
                                cl.sendMessage(to, None, contentMetadata={"STKID":"89547154","STKPKGID":"4834339","STKVER":"1"}, contentType=7) 
                                cl.sendMessage(to, None, contentMetadata={"STKID":"89547154","STKPKGID":"4834339","STKVER":"1"}, contentType=7) 

                        elif cmd.startswith("gemes"):
                          if wait["selfbot"] == True:
                           if msg._from in admin:  
                                cl.sendMessage(to, None, contentMetadata={"STKID":"12842266","STKPKGID":"1318245","STKVER":"1"}, contentType=7)                                    

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"KEBANYAKAN GOBLOK!")
                                        
                        elif cmd == "gcall":
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "{} Undangan Call Grup Berhasil".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"KEBANYAKAN BANGSAT!")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["message"]))
                                      ki.sendMessage(midd, str(Setmain["message"]))
                                      kk.sendMessage(midd, str(Setmain["message"]))
                                      kc.sendMessage(midd, str(Setmain["message"]))

#===========Settings============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
  
                        elif 'Cancell' in msg.text:
                           if msg._from in admin:
                             if msg.toType == 2:
                                 X = cl.getGroup(msg.to)
                                 if X.invitee is not None:
                                     gInviMids = [contact.mid for contact in X.invitee]
                                     random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                                 else:
                                     if wait["lang"] == "JP":
                                         cl.sendMessage(msg.to,"No one is inviting")
                                     else:
                                         cl.sendMessage(msg.to,"Sorry, nobody absent")
                             else:
                                 if wait["lang"] == "JP":
                                     cl.sendMessage(msg.to,"Can not be used outside the group")
                                 else:
                                     cl.sendMessage(msg.to,"Not for use less than group")      

                        elif 'Invite: ' in msg.text:
                           if msg._from in admin:
                             midd = msg.text.replace("Invite: ","")
                             cl.inviteIntoGroup(msg.to,[midd])                            
#===========Protection============#                                    

                        elif 'Protecturl ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'protectjoin ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)  
                                               
                        elif 'Antijs ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    

                        elif 'Satpro ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Satpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                #  if msg.to in protectjoin:
                                    #  msgs = ""
                                #  else:
                                    #  protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = ki.getGroup(msg.to)
                                      msgs = "ALL protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = ki.getGroup(msg.to)
                                      msgs = "Sudah mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "ALL protect sudah off\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Sudah menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Creatoradd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           creator[target] = True
                                           f=codecs.open('creator.json','w','utf-8')
                                           json.dump(creator, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           ki.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           kk.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           kc.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           kb.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           kd.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           ke.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           kf.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           kg.sendMessage(msg.to,"Berhasil menambahkan creator")
                                           kh.sendMessage(msg.to,"Berhasil menambahkan creator")
                                       except:
                                           pass

                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           ki.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           kk.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           kc.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           kb.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           kd.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           ke.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           kf.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           kg.sendMessage(msg.to,"Berhasil menambahkan admin")
                                           kh.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff[target] = True
                                           f=codecs.open('staff.json','w','utf-8')
                                           json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           ki.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           kk.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           kc.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           kb.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           kd.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           ke.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           kf.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           kg.sendMessage(msg.to,"Berhasil menambahkan staff")
                                           kh.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           ki.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           kk.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           kc.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           kb.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           kd.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           ke.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           kf.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           kg.sendMessage(msg.to,"Berhasil menambahkan bot")
                                           kh.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Creatordell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del creator[target]
                                           f=codecs.open('creator.json','w','utf-8')
                                           json.dump(creator, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           ki.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kk.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kc.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kb.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kd.sendMessage(msg.to,"Berhasil menghapus admin")
                                           ke.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kf.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kg.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kh.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass
                                           
                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           ki.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kk.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kc.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kb.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kd.sendMessage(msg.to,"Berhasil menghapus admin")
                                           ke.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kf.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kg.sendMessage(msg.to,"Berhasil menghapus admin")
                                           kh.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del staff[target]
                                           f=codecs.open('staff.json','w','utf-8')
                                           json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           ki.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           kk.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           kc.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           kb.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           kd.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           ke.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           kf.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           kg.sendMessage(msg.to,"Berhasil menghapus Staff")
                                           kh.sendMessage(msg.to,"Berhasil menghapus Staff")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.remove(target)
                                           ki.sendMessage(msg.to,"Berhasil menghapus bot")
                                           kk.sendMessage(msg.to,"Berhasil menghapus bot")
                                           kc.sendMessage(msg.to,"Berhasil menghapus bot")
                                           kb.sendMessage(msg.to,"Berhasil menghapus bot")
                                           kd.sendMessage(msg.to,"Berhasil menghapus bot")
                                           ke.sendMessage(msg.to,"Berhasil menghapus bot")
                                           kf.sendMessage(msg.to,"Berhasil menghapus bot")
                                           kg.sendMessage(msg.to,"Berhasil menghapus bot")
                                           kh.sendMessage(msg.to,"Berhasil menghapus bot")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in creator:
                                wait["addadmin"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "admin:dell" or text.lower() == 'admin:repeat':
                            if msg._from in creator:
                                wait["delladmin"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in creator:
                                wait["addstaff"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "staff:sell" or text.lower() == 'staff:repeat':
                            if msg._from in creator:
                                wait["dellstaff"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in creator:
                                wait["addbots"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in creator:
                                wait["dellbots"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in creator:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                ki.sendMessage(msg.to,"Refresh Done!")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = ki.getContact(i)
                                    ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                ki.sendMessage(msg.to,"Silahkan kirim kontaknya,\nJika sudah slesai, ketik invite off")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                ki.sendMessage(msg.to,"Invite via contact dinonaktifkan")
                               
                        elif cmd == "checkpost on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 ki.sendMessage(msg.to, "ᴄʜᴇᴄᴋᴘᴏsᴛ ᴏɴ")

                        elif cmd == "checkpost off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                ki.sendMessage(msg.to, "ᴄʜᴇᴄᴋᴘᴏsᴛ ᴏғғ")                                

                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["Mentionkick"] = True
                                ki.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["Mentionkick"] = False
                                ki.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["contact"] = True
                                ki.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["contact"] = False
                                ki.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["detectMention"] = True
                                ki.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["detectMention"] = False
                                ki.sendMessage(msg.to,"Auto respon dinonaktifkan")                   

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["autoJoin"] = True
                                ki.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["autoJoin"] = False
                                ki.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["autoLeave"] = True
                                ki.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["autoLeave"] = False
                                ki.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["autoAdd"] = True
                                ki.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["autoAdd"] = False
                                ki.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["sticker"] = True
                                ki.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["sticker"] = False
                                ki.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention2(msg.to, sender, "   sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ ɢʜᴅ\nᴜsᴇʀ: @! \nsᴇɴᴅ ʏᴏᴜʀ ᴘᴏsᴛ,\nʟɪᴋᴇ ᴅᴏɴᴇ-> ᴛᴏ ᴏғғ: ᴛɪᴍᴇʟɪɴᴇ ᴏғғ")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention2(msg.to, sender, "     sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ ɢʜᴅ\nᴜsᴇʀ: @! \nᴅᴇᴛᴇᴄᴛɪᴏɴ ᴛɪᴍᴇʟɪɴᴇ ᴏғғ")
                                
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                settings["autoJoinTicket"] = True
                                ki.sendMessage(msg.to,"Join ticket diaktifkan")
                                kk.sendMessage(msg.to,"Join ticket diaktifkan")
                                kc.sendMessage(msg.to,"Join ticket diaktifkan")
                                kb.sendMessage(msg.to,"Join ticket diaktifkan")
                                kd.sendMessage(msg.to,"Join ticket diaktifkan")
                                ke.sendMessage(msg.to,"Join ticket diaktifkan")
                                kf.sendMessage(msg.to,"Join ticket diaktifkan")
                                kg.sendMessage(msg.to,"Join ticket diaktifkan")
                                kh.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                settings["autoJoinTicket"] = False
                                ki.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                kk.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                kc.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                kb.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                kd.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                ke.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                kf.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                kg.sendMessage(msg.to,"Join Ticket dinonaktifkan")
                                kh.sendMessage(msg.to,"Join Ticket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           ki.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           kk.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           kc.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           kb.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           kd.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           ke.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           kf.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           kg.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                           kh.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           ki.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           kk.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           kc.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           kb.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           kd.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           ke.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           kf.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           kg.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                           kh.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["wblacklist"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                wait["dblacklist"] = True
                                ki.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              if wait["blacklist"] == {}:
                                ki.sendMessage(msg.to,"Tidak ada blacklist")
                                kk.sendMessage(msg.to,"Tidak ada blacklist")
                                kc.sendMessage(msg.to,"Tidak ada blacklist")
                                kb.sendMessage(msg.to,"Tidak ada blacklist")
                                kd.sendMessage(msg.to,"Tidak ada blacklist")
                                ke.sendMessage(msg.to,"Tidak ada blacklist")
                                kf.sendMessage(msg.to,"Tidak ada blacklist")
                                kg.sendMessage(msg.to,"Tidak ada blacklist")
                                kh.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +ki.getContact(m_id).displayName + "\n"
                                ki.sendMessage(msg.to,"»» Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              if wait["blacklist"] == {}:
                                    ki.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = ki.getContact(i)
                                        ki.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              wait["blacklist"] = {}
                              ragets = ki.getContacts(wait["blacklist"])
                              mc = "[%i]User Blacklist" % len(ragets)
                              kk.sendMessage(msg.to,"Sucses" )
                              kc.sendMessage(msg.to,"Sucses" )
                              kb.sendMessage(msg.to,"Sucses" )
                              kd.sendMessage(msg.to,"Sucses" )
                              ke.sendMessage(msg.to,"Sucses" )
                              kf.sendMessage(msg.to,"Sucses" )
                              kg.sendMessage(msg.to,"Sucses" )
                              kh.sendMessage(msg.to,"Sucses" )
                              ki.sendMessage(msg.to,"Kalian di maafkan " +mc)
#===========COMMAND SET============#
                        elif msg.contentType == 16:
                           if wait["Timeline"] == True:
                              msg.contentType = 0
                              msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                              ki.sendMessage(msg.to, "ʟɪᴋᴇ ᴅᴏɴᴇ ʙᴏss")
                              
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  ki.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  ki.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  ki.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  ki.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  ki.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  ki.sendMessage(msg.to, "「Leave Msg」\nLeave Msg diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  ki.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  ki.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  ki.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["message"] = spl
                                  ki.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in creator:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  ki.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  ki.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")
                               
                        elif text.lower() == "cek welcome":
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                                                

                        elif text.lower() == "cek respon":
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["message"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in creator:
                               ki.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")
  
#####============
                        elif text.lower() == "Hajar":
                          if msg.from_ in creator:
                           if msg.toType == 2:
                              print ("Ratain")
                              _name = msg.text.replace("Hajar","")
                              gs = cl.getGroup(msg.to)
                              cl.sendMessage(msg.to,"Hello Kk")
                              cl.sendMessage(msg.to,"Team BOTTROX Mau Bersih² Group Sampah Nih")
                              cl.sendMessage(msg.to,"Karna Ini Group Sampah Jadi Mau Di Bersihin Dulu Yah\n★Jangan Baper...\n★Jangan Nangis\n★Jangan Cengeng\nBawa Enjoy Aja Kawan♪")
                              cl.sendMessage(to,"┣━━╦━━━BOTTTOX TEAM━━━╦━━╣")
                              cl.sendContact(to, mid)
                              cl.sendContact(to, Amid)
                              cl.sendContact(to, Bmid)
                              cl.sendContact(to, Cmid)
                              cl.sendContact(to, Dmid)
                              cl.sendContact(to, Emid)
                              cl.sendContact(to, Fmid)
                              cl.sendContact(to, Gmid)
                              cl.sendContact(to, Imid)
                              cl.sendContact(to, Jmid)
                              cl.sendMessage(to,"┣━━╦━━━BOTTTOX TEAM━━━╦━━╣")
                              cl.sendMessage(msg.to,"This My Team")
                              targets = []
                              for g in gs.members:
                                if _name in g.displayName:
                                  targets.append(g.mid)
                              if targets == []:
                                cl.sendMessage(msg.to,"Not found")
                              else:
                                for target in targets:
                                  if target in admin:
                                    pass
                                  elif target in Bots:
                                    pass
                                  elif target in staff:
                                    pass
                                  else:
                                    try:
                                      klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      #print (msg.to,[g.mid])
                                    except:
                                      try:
                                        cl.kickoutFromGroup(msg.to,[target])
                                      except:
                                        random.choice(KAC).kickoutFromGroup(msg.to,[target])

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "OTW JOIN GROUP : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "JOIN GROUP : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "OTW JOIN GROUP : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "OTW JOIN GROUP : %s" % str(group.name))
                                     group4 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kb.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = kd.findGroupByTicket(ticket_id)
                                     kd.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kd.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group6 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ke.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group7 = kf.findGroupByTicket(ticket_id)
                                     kf.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kf.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group8 = kg.findGroupByTicket(ticket_id)
                                     kg.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kg.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group9 = kh.findGroupByTicket(ticket_id)
                                     kh.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kh.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
                               