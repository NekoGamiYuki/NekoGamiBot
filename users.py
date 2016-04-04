import communication as comm
import moderation

class User(object):
    """
    This class contains simple information about the users within chat.

    You can get their name, message, and what channel they chatted from.
    You can also send them messages (@username in chat). By default it
    sends a message back to where they chatted from, but you can change
    the channel if you wish to, for whatever reason.

    usage:
    newuser = User(response_from_twitch_server)
    print(newuser.get_name())
    print(newuser.get_message())
    print(newuser.get_channel_from())
    """
    def __init__(self,response):
        # Why the try block? Because the first few messages from twitch
        # cause some issues and I haven't found a better way to handle
        # them yet. 
        try:
            self.info = response.split(':')
            self.message = self.info[2].rstrip()
            self.name = self.info[1].split("!")[0]
            self.channel_from = self.info[1].split('#')[1]
        except:
            self.message = "MESSAGE_UNAVAILABLE"
            self.name = "NAME_UNAVAILABLE"
            self.channel_from = "CHANNEL_UNAVAILABLE"
    
    def get_name(self):
            return self.name

    def get_message(self):
            return self.message.encode()

    def get_channel_from(self):
            return self.channel_from

    def send_message(self,sock,message,channel=None):
        # For some reason I couldn't do "channel=self.channel_from" in the
        # arguments. so I'm going to do it here...
        if channel == None:
            channel = self.channel_from

        comm.chat(message,channel,sock)

    def timeout(self,sock,seconds=5,reason=None):
        moderation.timeout_user(self.name,seconds,self.channel_from,sock)
