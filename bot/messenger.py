# -*- coding: utf-8 -*-

import logging
import random
import sys  

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
            "Hi :wave:, who doesnt like a good quote ?",
            "> `hi <@" + bot_uid + ">` - I'll respond with a randomized greeting mentioning you. :wave:",
            "> `<@" + bot_uid + "> Quote` - I'll tell you one of my finest quotes"
			)
        self.send_message(channel_id, txt)

    def write_greeting(self, channel_id, user_id):
        greetings = ["Do you feel lucky ....", "Greetings ....","Winter is coming...", "Valar Morghulis...","Say hello to my little friend...","You talkin to me .."]
        txt = '{} <@{}>!'.format(random.choice(greetings), user_id)
        self.send_message(channel_id, txt)

    def write_prompt(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "Whoa ... spell it out for me.. please ? (e.g. `<@" + bot_uid + "> help`)"
        self.send_message(channel_id, txt)

    def write_quote(self, channel_id):
		quotes=["To infinity…and beyond!","I have come here to chew bubblegum and kick ass, and I'm all out of bubblegum.","Surely, you cant be serious – I am serious, and don't call me Shirley.","I pity the fool","There can be only @juantwothree","THIS IS SPARTA!!!!","Shit just got real","It's clobberin time!","Go ahead, make my day....","Run, Forrest, run!!!","I'm too old for this shit..","I'll be back","SHOW ME THE MONEY!!!","Greed, for lack of a better word, is good..","You can't handle the truth!","Snap out of it!","I feel the need…the need for speed :top: :gun: ","You're gonna need a bigger boat","I see dead people","Great scott!","Life is like a box of chocolates :chocolate_bar: you never know what youre gonna get","I'm gonna make him an offer he can't refuse","They may take our lives, but they'll never take…OUR FREEDOM :crossed_swords: !!!","Oh, behave!","You had me at hello","I'm not bad...I'm just drawn that way",":trollface: Ssssssssssssmokin :trollface:","I'll have what shes having","Wax on, wax off. Wax on, wax off","Hakuna Matata","I'm sorry,Sharpy...I'm afraid I cant do that",":spock-hand::skin-tone-2: Live long and prosper :spock-hand::skin-tone-2:"]
		txt = random.choice(quotes)
   		self.clients.send_user_typing_pause(channel_id)
		self.send_message(channel_id, txt)
		
    def write_quoteBB(self, channel_id):
		quotesBB=["A guy opens his door and gets shot and you think that of me? No...I AM THE ONE WHO KNOCKS","Whats the point of being an outlaw when you got responsibilities?","Stay out of my territory","This is my own private domicile and I will not be harassed…bitch!"]
		txt = random.choice(quotesBB)
		BBintro = ["I'm glad you noticed... enjoy my next quote then", "I'm glad you asked...lemme see what i can find for ya.","very observant ....Bitch... let me find a good one for you","Do you also think blue is my favorite colour ? you are 99.1% right ..now for that quote..."]
		self.clients.send_user_typing_pause(channel_id)
		self.send_message(channel_id, BBintro)
		self.clients.send_user_typing_pause(channel_id)
		self.send_message(channel_id, txt)
		
    def write_error(self, channel_id, err_msg):
        txt = ":face_with_head_bandage: Houston, we have a problem :\n>```{}```".format(err_msg)
        self.send_message(channel_id, txt)
