# A dictionary of all the options within the config file.
options  = {}

def create_config():
    """
    Attempts to create a config file. It loads the default values and leaves 
    placeholders for uesr information. If it succeeds, it returns 0, else it
    returns 1.

    WARNING: It is highly recommended that you test for load_config() before
    running create_config(), as create_config() will ALWAYS create a new
    config file. This means that if a config file already exists, it will be
    overwritten.

    Default values:
    HOST=irc.twitch.tv
    PORT=6667
    NICK=YOUR_BOT_NICK_HERE
    PASS=YOUR_OAUTH_HERE (Generate one here: https://twitchapps.com/tmi/)
    CHANNELS=CHANNEL1, CHANNEL2, ETC...
    CHAT_RATE=100
    """
    try:
        config_file = open("config",'w')
        config_file.write("HOST=irc.twitch.tv\n"
                          "PORT=6667\n"
                          "NICK=YOUR_BOT_NICK_HERE\n"
                          "OAUTH=YOUR_OAUTH_HERE (Generate one here: https://twitchapps.com/tmi/)\n"
                          "CHANNELS=CHANNEL1, CHANNEL2, ETC...\n"
                          "CHAT_RATE=100\n")
        config_file.close()
        return 0
    except:
        return 1


def load_config():
    """
    Attempts to load the config file. If it succeeds, it places the data into
    the following variables and returns 0. If it fails, it returns 1.

    HOST: The IRC server
    PORT: The port we will attempt to conenct through
    NICK: The user's nickname
    OAUTH: The twitch OAUTH, can be generated here https://twitchapps.com/tmi/
    CHANNELS: The channel, or channels you'd like to connect to
    CHAT_RATE: How fast the bot is able to chat, per minute. 
               The default is 100, as this is how fast a Moderator may chat
    """

    global options
    
    try:
        config_file = open("config", 'r')
        config_variables = config_file.readlines()

        #Fill in the options dictionary with the inforamtion from the config file.
        #This code will hopefully make it so that I can easily expand the config
        #file when necessary
        for line in config_variables:
            options[line.split("=")[0]] = line.split("=")[1].rstrip()

        config_file.close()
        return 0
    except:
        return 1
