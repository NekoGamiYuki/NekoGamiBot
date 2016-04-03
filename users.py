class User(object):

    def __init__(self,response):
        try:
            self.info = response.split(':')
            self.message = self.info[2]
            self.name = self.info[1].split("!")[0]
            self.channel_from = self.info[1].split('#')[1]
        except:
            pass
            
    def get_name(self):
        try:
            return self.name
        except:
            return "NAME_UNAVAILABLE"

    def get_message(self):
        try:
            return self.message.rstrip()
        except:
            return "MESSAGE_UNAVAILABLE"

    def get_channel_from(self):
        try:
            return self.channel_from
        except:
            return "CHANNEL_UNAVAILABLE"
