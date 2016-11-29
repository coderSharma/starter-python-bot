import json
import logging
import re

from slacker import Slacker
from slackclient import SlackClient

logger = logging.getLogger(__name__)


class RtmEventHandler(object):
    def __init__(self, slack_clients, msg_writer):
        self.clients = slack_clients
        self.msg_writer = msg_writer

    def handle(self, event):

        if 'type' in event:
            self._handle_by_type(event['type'], event)

    def _handle_by_type(self, event_type, event):
        # See https://api.slack.com/rtm for a full list of events
        if event_type == 'error':
            # error
            self.msg_writer.write_error(event['channel'], json.dumps(event))
        elif event_type == 'message':
            # message was sent to channel
            self._handle_message(event)
        elif event_type == 'channel_joined':
            # you joined a channel
            self.msg_writer.write_help_message(event['channel'])
        elif event_type == 'group_joined':
            # you joined a private group
            self.msg_writer.write_help_message(event['channel'])
        else:
            pass

    def is_quote_mention(self, message):
        if re.search('quotes|quote|movie reference|movie references', message):
            return True
        else:
            return False

    def is_BB_mention(self, message):
        if re.search('bb reference|BB reference|breaking bad|jesse pinkman|heisenberg|Heisenberg|bb references|BB||bb|Walter White|walter white', message):
            return True
        else:
            return False            
            
    def is_name_mention(self, message):
        if re.search('say my name|SAY MY NAME|SAY my NAME|say MY name|SaY mY nAmE', message):
            return True
        else:
            return False
            
    def request_greeting(self, message):
        if re.search('hi quotebot|hey quotebot|hello quotebot|howdy quotebot|hi Quotebot|hey Quotebot|hello Quotebot|howdy Quotebot|hello bot|Hello Quotebot|hola quotebot|hola Quotebot|Morning Quotebot|hi quoteBot|hey quoteBot|hello quoteBot|howdy quoteBot|hi QuoteBot|hey QuoteBot|hello QuoteBot|howdy QuoteBot|hello Bot|Hello QuoteBot|hola quoteBot|hola QuoteBot|Morning QuoteBot', message):
            return True
        else:
            return False

    def is_creator_mention(self, message):
        if re.search('who is your creator| who created you|who created quotebot', message):
            return True
        else:
            return False        
    
    def _handle_message(self, event):
        # Filter out messages from the bot itself, and from non-users (eg. webhooks)
        if ('user' in event) and (not self.clients.is_message_from_me(event['user'])):
        #if not self.clients.is_message_from_me(event['user']): 
            msg_txt = event['text']
            if (self.clients.is_bot_mention(msg_txt) or self.is_quote_mention(msg_txt) or self.is_creator_mention(msg_txt) or self.is_name_mention(msg_txt) or self.request_movie_quote(msg_txt) or self.is_BB_mention(msg_txt)) :
                # e.g. user typed a direct message or Quotebot was listening for a keyword shout a quote!"
                    if 'help' in msg_txt:
                        self.msg_writer.write_help_message(event['channel'])
                    elif re.search('hi quotebot|hey quotebot|hello quotebot|howdy quotebot|hi Quotebot|hey Quotebot|hello Quotebot|howdy Quotebot|hello bot|Hello Quotebot|hola quotebot|hola Quotebot|Morning Quotebot|hi quoteBot|hey quoteBot|hello quoteBot|howdy quoteBot|hi QuoteBot|hey QuoteBot|hello QuoteBot|howdy QuoteBot|hello Bot|Hello QuoteBot|hola quoteBot|hola QuoteBot|Morning QuoteBot', msg_txt):
                        self.msg_writer.write_greeting(event['channel'], event['user'])
                    elif re.search('quotes|quote|movie reference|movie references', msg_txt):
                        self.msg_writer.write_quote(event['channel'])
                    elif re.search('bb reference|BB reference|breaking bad|jesse pinkman|heisenberg|Heisenberg|bb references|BB||bb|Walter White|walter white', msg_txt):
                        self.msg_writer.write_quoteBB(event['channel'])
                    elif re.search('who is your creator| who created you|who created quotebot', msg_txt):
                        self.msg_writer.write_quoteCreator(event['channel'])
                    elif re.search('say my name|SAY MY NAME|SAY my NAME|say MY name|SaY mY nAmE', msg_txt):
                        self.msg_writer.write_name(event['channel'],event['user'])
                    elif re.search('quote from|quote from movie|Quote from movie|Quote from', msg_txt):
                        self.msg_txt.get_quote(['channel'],event['user'])
                    else:
                        self.msg_writer.write_prompt(event['channel'])
