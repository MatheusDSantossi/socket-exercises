import socket, select, string, sys

#Helper function (formatting)
def display() :
	you="\33[33m\33[1m"+" You: "+"\33[0m"
	sys.stdout.write(you)
	sys.stdout.flush()

def main():

    if len(sys.argv)<2:
        host = input("Enter host ip address: ")
    else:
        host = sys.argv[1]

    port = 5001
    
    #asks for user name
    name = input("34m\33[1m CREATING NEW ID:\n Enter username: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    # connecting host
    try :
        s.connect((host, port))
    except :
        print("Can't connect to the server")
        sys.exit()

    #if connected
    s.send(name)
    display()
    while 1:
        socket_list = [sys.stdin, s]
        
        # Get the list of sockets which are readable
        rList, wList, error_list = select.select(socket_list , [], [])
        
        for sock in rList:
            #incoming message from server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print('\rDISCONNECTED!!\n')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    display()
        
            #user entered a message
            else :
                msg=sys.stdin.readline()
                s.send(msg)
                display()

if __name__ == "__main__":
    main()