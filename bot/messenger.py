# -*- coding: utf-8 -*-

import logging
import random

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
        greetings = ['Do you feel lucky ....', 'Greetings ....', 'Winter is coming...', 'Valar Morghulis...','Say hello to my little friend...','You talkin’ to me ..']
        txt = '{} <@{}>!'.format(random.choice(greetings), user_id)
        self.send_message(channel_id, txt)

    def write_prompt(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "I'm sorry, I didn't quite understand... Can I help you? (e.g. `<@" + bot_uid + "> help`)"
        self.send_message(channel_id, txt)

    def write_quote(self, channel_id):
		self.clients.send_user_typing_pause(channel_id)
		quotes=["To infinity…and beyond!","I have come here to chew bubblegum and kick ass, and I’m all out of bubblegum.","Surely, you can’t be serious.” – “I am serious, and don’t call me Shirley.","I pity the fool","There can be only @juantwothree","THIS IS SPARTA!!!!","Shit just got real","It’s clobberin’ time!","Go ahead, make my day....","Run, Forrest, run!!!","I’m too old for this shit..","I’ll be back","SHOW ME THE MONEY!!!","Greed, for lack of a better word, is good..","You can’t handle the truth!","Snap out of it!","I feel the need…the need for speed","You’re gonna need a bigger boat","I see dead people","Great scott!","Life is like a box of chocolates: you never know what you’re gonna get","I’m gonna make him an offer he can’t refuse","They may take our lives, but they’ll never take…OUR FREEDOM!","Oh, behave!","You had me at ‘hello’","I’m not bad. I’m just drawn that way","Ssssssssssssmokin","I’ll have what she’s having","Wax on, wax off. Wax on, wax off","Hakuna Matata","I’m sorry,@sharpy...I’m afraid I can’t do that",":spock-hand::skin-tone-2: Live long and prosper :spock-hand::skin-tone-2:"]
   		self.send_message(channel_id, quotes)
		
	def write_quoteBB(self, channel_id):
		self.clients.send_user_typing_pause(channel_id)
		quotesBB=["A guy opens his door and gets shot and you think that of me? No...I AM THE ONE WHO KNOCKS","What’s the point of being an outlaw when you got responsibilities?","Stay out of my territory","This is my own private domicile and I will not be harassed…bitch!"]
   		self.send_message(channel_id, quotesBB)
			
    def write_error(self, channel_id, err_msg):
        txt = ":face_with_head_bandage: Houston, we have a problem :\n>```{}```".format(err_msg)
        self.send_message(channel_id, txt)
