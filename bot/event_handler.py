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

    def is_quote_mention(message):
        if re.search('quotes', message):
            return True
        else:
            return False
	
    def _handle_message(self, event):
        # Filter out messages from the bot itself, and from non-users (eg. webhooks)
        #if ('user' in event) and (not self.clients.is_message_from_me(event['user'])):
        if not self.clients.is_message_from_me(event['user']): 
            msg_txt = event['text']

            if (self.clients.is_bot_mention(msg_txt)) or (self.clients.is_quote_mention(msg_txt)) :
                # e.g. user typed: "@pybot shout a quote!"
                if 'help' in msg_txt:
                    self.msg_writer.write_help_message(event['channel'])
                elif re.search('hi|hey|hello|howdy|hello bot|hello Quotebot|hi quotebot', msg_txt):
                    self.msg_writer.write_greeting(event['channel'], event['user'])
                elif 'quote' in msg_txt:
                    self.msg_writer.write_quote(event['channel'])
                elif 'attachment' in msg_txt:
                    self.msg_writer.demo_attachment(event['channel'])
                elif 'echo' in msg_txt:
                    self.msg_writer.send_message(event['channel'], msg_txt)
                else:
                    self.msg_writer.write_prompt(event['channel'])
