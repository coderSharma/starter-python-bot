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
        greetings = ["Do you feel lucky ....", "Greetings ....","Winter is coming...", "Valar Morghulis...","Say hello to my little friend...","You talkin’ to me .."]
        txt = '{} <@{}>!'.format(random.choice(greetings), user_id)
        self.send_message(channel_id, txt)

    def write_prompt(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "Whoa ... spell it out for me ? (e.g. `<@" + bot_uid + "> help`)"
        self.send_message(channel_id, txt)

    def write_quote(self, channel_id):
		self.clients.send_user_typing_pause(channel_id)
		quotes=["To infinity…and beyond!"]
   		self.send_message(channel_id, quotes)
		
    def write_quoteBB(self, channel_id):
		self.clients.send_user_typing_pause(channel_id)
		quotesBB=["A guy opens his door and gets shot and you think that of me? No...I AM THE ONE WHO KNOCKS","What’s the point of being an outlaw when you got responsibilities?","Stay out of my territory","This is my own private domicile and I will not be harassed…bitch!"]
		self.send_message(channel_id, quotesBB)
		
    def write_error(self, channel_id, err_msg):
        txt = ":face_with_head_bandage: Houston, we have a problem :\n>```{}```".format(err_msg)
        self.send_message(channel_id, txt)
