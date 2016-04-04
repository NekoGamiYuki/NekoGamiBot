import communication as comm

def timeout_user(user, seconds, channel, sock):
    comm.chat(".timeout %s %d" %(user, seconds), channel, sock)

