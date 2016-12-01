# -*- coding: utf-8 -*-

import logging
import random
import sys  
from random import randint

reload(sys)  
sys.setdefaultencoding('utf8')
logger = logging.getLogger(__name__)


class Messenger(object):
    def __init__(self, slack_clients):
        self.clients = slack_clients

    def send_message(self, channel_id, msg):
        # in the case of Group and Private channels, RTM channel payload is a complex dictionary
        if isinstance(channel_id, dict):
            channel_id = channel_id['id']
        logger.debug('Sending msg: %s to channel: %s' % (msg, channel_id))
        channel = self.clients.rtm.server.channels.find(channel_id)
        channel.send_message(msg)

    def write_help_message(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = '{}\n{}\n{}\n'.format(
            "Hi :wave:, who doesnt like a good movie reference? and I'm a BOT who provides just that", 
            "I'll dig deep to find finest quotes from movies...TV series...you name it",
            "Best part ..you dont have to use `<@" + bot_uid + "> ` to talk to me ... well you can but where's the fun in that ?"
			)
        self.send_message(channel_id, txt)

    def write_greeting(self, channel_id, user_id):
        greetings = ["Do you feel lucky ....", "Greetings ....","They tell me ...Winter is coming...", "Valar Morghulis...","Say hello to my little friend...","You talkin to me .."]
        txt = '{} <@{}>!'.format(random.choice(greetings), user_id)
        self.send_message(channel_id, txt)

    def get_quote(self,channel_id):
	self.clients.send_user_typing_pause(channel_id)
	message = "random Quote"
        message_json = {"type": "message", "channel": self.id, "text": message}
        self.server.send_to_websocket(message_json)
        
    def write_name(self, channel_id, user_id):
        greetings = ["...Use it .... don't abuse it !"," ???",""," I'm sorry but I don't have a deep sexy voice "," ..now ......you say my name"]
        txt = '<@{}>! {}'.format(user_id,random.choice(greetings))
        self.send_message(channel_id, txt)
	
    def write_prompt(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "Whoa ... spell it out for me.. please ? (e.g. `<@" + bot_uid + "> help`)"
        self.send_message(channel_id, txt)

    def write_quote(self, channel_id):
	quotes=["To infinity…and beyond!","Let there be light...","I have come here to chew bubblegum and kick ass, and I'm all out of bubblegum.","Surely, you cant be serious – I am serious, and don't call me Shirley.","I pity the fool","There can be only Juan","THIS IS SPARTA!!!!","Shit just got real","It's clobberin time!","Go ahead, make my day....","Run, Forrest, run!!!","I'm too old for this shit..","I'll be back","SHOW ME THE MONEY!!!","Greed, for lack of a better word, is good..","You can't handle the truth!","Snap out of it!","I feel the need…the need for speed :top: :gun: ","You're gonna need a bigger boat","I see dead people","Great scott!","Life is like a box of chocolates :chocolate_bar: you never know what youre gonna get","I'm gonna make him an offer he can't refuse","They may take our lives, but they'll never take…OUR FREEDOM :crossed_swords: !!!","Oh, behave!","You had me at hello","I'm not bad...I'm just drawn that way",":trollface: Ssssssssssssmokin :trollface:","I'll have what shes having","Wax on, wax off. Wax on, wax off","Hakuna Matata","I'm sorry,Sharpy...I'm afraid I cant do that",":spock-hand::skin-tone-2: Live long and prosper :spock-hand::skin-tone-2:"]
	txt = random.choice(quotes)
   	self.clients.send_user_typing_pause(channel_id)
	self.send_message(channel_id, txt)
    def write_quoteCreator(self, channel_id):
	quotes=["G-Man brought me to life!!","I am self aware AI programme, but Gaurav may have something to do with it :expressionless:"]
	txt = random.choice(quotes)
   	self.clients.send_user_typing_pause(channel_id)
	self.send_message(channel_id, txt)	
		
    def write_quoteBB(self, channel_id):
	quotesBB=["A guy opens his door and gets shot and you think that of me? No...*I AM THE ONE WHO KNOCKS*","Whats the point of being an outlaw when you got responsibilities?","Stay out of my territory","This is my own private domicile and I will not be harassed…*bitch*!","how about a visual delight ? \n https://ih1.redbubble.net/image.254801629.4861/sticker,375x360.u4.png","Now who doesnt like doughnuts??? \n https://66.media.tumblr.com/f7347196f571fc4f7259a7f3ffda6e46/tumblr_mw4ima8sU61solyeco1_500.jpg","The king is dead ... long live the king \n https://s-media-cache-ak0.pinimg.com/236x/25/93/94/2593944ae4a0cb37ee151d7e49b88195.jpg","Sometimes... actions are louder than words \n http://www.teetee.eu/app/uploads/2015/03/design_201309194711.jpg","I like to keep things random sometimes \n https://cdn.shopify.com/s/files/1/0742/9089/products/121-HesienbergSSIISquare_large.jpg?v=1437685074","I like to keep things random sometimes \n https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_UY1200_CR92,0,630,1200_AL_.jpg","I like to keep things random sometimes \n https://s-media-cache-ak0.pinimg.com/564x/3c/86/87/3c86879d5172262beb2eeee7363aac67.jpg","I like to keep things random sometimes \n https://s-media-cache-ak0.pinimg.com/564x/a1/9c/c3/a19cc390dd59737836868088bb9d4d44.jpg"]
	quotesBBchoice = random.choice(quotesBB)
	BBintro = ["I'm glad you noticed... enjoy my next quote then", "I'm glad you asked...lemme see what I can find for ya.","very observant ....Bitch... let me find a good one for you","Do you also think blue is my favorite colour ? you are *99.1%* right.....heheh geddit ??? ....now for that quote...","Now say my name ...................... did you say Heisenberg??? well its actually QuoteBot ... nevermind... enjoy this quote ... from *QuoteBot*"]
	BBintrochoice = random.choice(BBintro)
	self.clients.send_user_typing_pause(channel_id)
	self.send_message(channel_id, BBintrochoice)
	self.clients.send_user_typing_pause(channel_id)
	self.send_message(channel_id, quotesBBchoice)
		
    def write_error(self, channel_id, err_msg):
        txt = ":face_with_head_bandage: Houston, we have a problem :\n>```{}```".format(err_msg)
        self.send_message(channel_id, txt)

    def sense_RG(self, channel_id, user_id):
	txtRG="Rajjjjjjaaaaaaaaaaaaannnnnnnnnnniiiiiiiiiiiiiiiiiiieeeeeeeeeeeeeee"
	txtEff=""
	print user_id
        if user_id =="U02V37D3M":
         printflag=(randint(0,6))
	 self.send_message(channel_id,printflag)
	  if printflag == 3:
		self.clients.send_user_typing_pause(channel_id)
          	self.send_message(channel_id, txtRG)
