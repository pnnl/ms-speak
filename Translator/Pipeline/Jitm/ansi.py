# begin code

#!/usr/bin/env python
'''
ansi.py

ANSI Terminal Interface

Color Usage:
print RED + 'this is red' + RESET
print BOLD + GREEN + WHITEBG + 'this is bold green on white' + RESET

Commands:
def move(new_x, new_y): 'Move cursor to new_x, new_y'
def moveUp(lines): 'Move cursor up # of lines'
def moveDown(lines): 'Move cursor down # of lines'
def moveForward(chars): 'Move cursor forward # of chars'
def moveBack(chars): 'Move cursor backward # of chars'
def save(): 'Saves cursor position'
def restore(): 'Restores cursor position'
def clear(): 'Clears screen and homes cursor'
def clrtoeol(): 'Clears screen to end of line'
'''
import sys,os
import struct
import socket

#from subprocess import Popen, PIPE

# None is returned on success. On error, an exception is raised, and 
# there is no way to determine how much data, if any, was successfully sent.
def send_msg(sock, msg):
    try:
        # Prefix each message with a 4-byte length (network byte order)
        #msglen = len(msg)
        #print "Sending {} bytes.".format( msglen)
        #msg = struct.pack('>I', msglen) + msg
        # None is returned on success. On error, an exception is raised, and 
        # there is no way to determine how much data, if any, was successfully sent.
        s = sock.sendall(msg)
        return s
    except Exception as e:
        raise e
    
def recv_msg(sock):
    try:
        # Read message length and unpack it into an integer
        raw_msglen = recvall(sock, 4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        # Read the message data
        #print "Received {}-byte length msg.".format( raw_msglen)
        r =  recvall(sock, msglen)
        #r =  sock.recv( 8192)
        
        return r
    except Exception as e:
        raise e
'''
to be able to tell when the server sockets is closed
don't even specify setblocking at all
set tmo via settimeout(2)

then expect to handle exception on timeout on good socket with no data
and for bad socket, no exception but returns None
'''
def recvall(sock, n):
    try:
        # Helper function to recv n bytes or return None if EOF is hit
        data = ''
        while len(data) < n:
            packet = sock.recv(n - len(data))
            if not packet:# since our socket uses a tmo that throws e, this means socket is closed at other end
                raise socket.error
                #return None
            data += packet
        return data
    except Exception as e:
        raise e

def wait_key():
    print 'Waiting for key press...'
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()
        try:  # if not running in a terminal, i.e., from Eclipse, the following fails
            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
        except:
            result = sys.stdin.readline().strip('\n')
        else:
            try:
                result = sys.stdin.read(1)
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            except:# catch exit via ctrl-c etc. and restore
                #print "Restoring termios..."
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                raise

    return result

################################
# C O L O R C O N S T A N T S #
################################
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

RESET = '\033[0;0m'
BOLD = '\033[1m'
REVERSE = '\033[2m'

BLACKBG = '\033[40m'
REDBG = '\033[41m'
GREENBG = '\033[42m'
YELLOWBG = '\033[43m'
BLUEBG = '\033[44m'
MAGENTABG = '\033[45m'
CYANBG = '\033[46m'
WHITEBG = '\033[47m'

def move(new_x, new_y):
    'Move cursor to new_x, new_y'
    print '\033[' + str(new_x) + ';' + str(new_y) + 'H'
    
def moveUp(lines):
    'Move cursor up # of lines'
    print '\033[' + str(lines) + 'A'

def moveDown(lines):
    'Move cursor down # of lines'
    print '\033[' + str(lines) + 'B'

def moveForward(chars):
    'Move cursor forward # of chars'
    print '\033[' + str(chars) + 'C'

def moveBack(chars):
    'Move cursor backward # of chars'
    print '\033[' + str(chars) + 'D'

def save():
    'Saves cursor position'
    print '\033[s'

def restore():
    'Restores cursor position'
    print '\033[u'

' http://askubuntu.com/questions/25077/how-to-really-clear-the-terminal'
def clear():
    'Clears screen and homes cursor'
    if os.name == 'nt':
        os.system('cls')
    else:
        #print '\033[2J'
        #os.system('clear') # causes 'emacs': unknown terminal type.
        #sys.stderr.write("\x1b[2J\x1b[H") # cause [2J[H
        #print("\033c") # causes c
        #os.system('tput reset')
        os.system('printf "\033c"')
        #os.system('reset')

def reset():
    'Clears screen and homes cursor to 0,0'
    clear()
    move( 0,0 )

def clrtoeol():
    'Clears screen to end of line'
    print '\033[K'

def print_there(x, y, text, clearscreen=False):

    if( clearscreen ):
        clear()
    '''
    if os.name == 'nt':
        if( clearscreen ):
            os.system('cls')
    else:
        if( clearscreen ):
            # os.system('clear')
            sys.stderr.write("\x1b[2J\x1b[H")  # clear screen, move cursor to top
            #print(chr(27) + "[2J") # clear screen

    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()
    '''
    move(x, y)
    sys.stdout.write( text )

# ======end code=======
'''
def SSLSend(msg):
    # i = msg.find('<tns:ODEventNotification xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"')
    # j = msg.find('</tns:ODEventNotification>')
    # msg = msg[i:j+26]
    args = ['./sslconnect', '--file', '-']
    print(msg)  # DEBUG
    try:
        # Create a TCP socket (client)
        p = Popen(args, stdin=PIPE, stdout=PIPE)
        sent = 0
        #print("subprocess success!")
        while sent < len(msg):
            #print('Sending', sent, 'bytes...')  # DEBUG
            try:
                p.stdin.write(msg[sent:sent+MSG_LENGTH].encode())
            except:
                print('Failed to Send')
            sent += MSG_LENGTH
        try:
            p.stdin.close()
            p.stdout.close()
        except:
            print('Failed to Close')
    except Exception as e:
        print('ERROR: Could not connect to the server: %s', e)
'''
