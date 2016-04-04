class User(object):
    """
    This class contains simple information about the users within chat.

    You can get their name, message, and what channel they chatted from.

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
            return self.message.rstrip()


    def get_channel_from(self):
            return self.channel_from

