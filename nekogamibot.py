#-------------------------------------------------------------------------------
# NekoGamiBot (VERSION: 0.1.0)
#
# Created by NekoGamiYuki
#
# As of Sat Apr 2, I have begun development on NekoGamiBot. The goal, for now,
# is to make a bot that has basic features. 
#
# Those features are as follows:
#     - Filtering of chat, timing out based on specific settings (such as timing
#       out links)
#     - Simple command/response system (!status |"Everything seems fine to me!")
#-------------------------------------------------------------------------------

#Modules------------------------------------------------------------------------
import sys #For exiting the program prematurely
import socket #For the actual connection to twitch and network communication!
import time #For the sleep function and seeing how much time has passed
import configuration as config #Managing bot configuration
import communication as comm #So that we can communicate with twitch/twitch chat
import users # User management

#-------------------------------------------------------------------------------

#Reading/Creating Config File---------------------------------------------------
print("Attempting to load config file...")
if config.load_config() == 1:
    print("Unable to load config file.")
    print("Attempting to create config file...")
    
    if config.create_config() == 0:
        print("Created config file.")
    elif config.create_config() == 1:
        print("Unable to create config file. Fuck...")
        sys.exit(1)

    print("Please go and edit the config file to your needs, then restart the "
          "program")
    sys.exit(0)
elif config.load_config() == 0:
    print("Configuration loaded.")

#-------------------------------------------------------------------------------

#Connecting to Twitch-----------------------------------------------------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to twitch...")
sock.connect((config.options["HOST"], int(config.options["PORT"])))

print("Sending OAUTH...")
comm.info_to_twitch("PASS %s\r\n" %(config.options["OAUTH"]), sock)

print("Sending Username...")
comm.info_to_twitch("NICK %s\r\n" %(config.options["NICK"]), sock)

for channel in config.options["CHANNELS"].split(','):
    print("Joining %s..." %(channel))
    comm.info_to_twitch("JOIN #%s\r\n" %(channel), sock)

print("Finished joining channels.")

#-------------------------------------------------------------------------------

#Getting Chat Messages and Twitch Information-----------------------------------
while True:
    response = sock.recv(1024)
    user = users.User(response.decode())
    print(user.get_name())
    print(user.get_message())
    print(user.get_channel_from())

        
    time.sleep(0.01) #Receive 100 responses from twitch per minute.
