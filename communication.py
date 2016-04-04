import configuration as config
import time

CHAT_COUNT = 0
ALLOW_CHATTING = True
PREVIOUS_MESSAGE_TIME = 0.0
TIME_ELAPSED = 0.0


def info_to_twitch(info, sock):
    """
    Sends raw data over to twitch.

    This is to be used for sending things like "PONG, JOIN, PASS, NICK" and such.

    If you need to send messages to chat, use the chat() function

    Example: 
    info_to_twitch("JOIN #nekogamibot\r\n", socket)
    """
    sock.sendto(info.encode(), (config.options["HOST"], int(config.options["PORT"])))

def chat(message, chan, sock):
    """
    Sends a message over to a specific twitch channel's chat. It also tries to
    stay within the boundaries set by the "RATE" option in the config file.

    This is what you'll likely use the most.

    Example:
    chat("PogChamp HYPE!", "nekogamibot", socket)
    """
    global CHAT_COUNT
    global ALLOW_CHATTING
    global PREVIOUS_MESSAGE_TIME
    global TIME_ELAPSED
    
    TIME_ELAPSED = time.time() - PREVIOUS_MESSAGE_TIME
    print(TIME_ELAPSED)
    if TIME_ELAPSED > (1.0/float(config.options["CHAT_RATE"])) and ALLOW_CHATTING == True:
        final_message = "PRIVMSG #%s :%s\r\n" %(chan, message)
        sock.sendto(final_message.encode(), (config.options["HOST"], int(config.options["PORT"])))
    else:
        pass

    PREVIOUS_MESSAGE_TIME = time.time()
