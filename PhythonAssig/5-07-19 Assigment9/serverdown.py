# Sometimes servers are down, so clients cannot connect to them.
# Python raises an exception of type ConnectionRefusedError in a client program when a network connection is refused.
# Add code to the day/time client program to catch and recover from this kind of exception.(Use timeClientServer_starter.zip)

for ip in ips:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try :
        sock.connect((ip,12345))
        print("Up.")
        up.append(ip)
        sock.close()
    except OSError:
        print("Down.")
        raise
    except ConnectionRefusedError:
        print("Up.")
        up.append(ip)
    except Exception as e:
        print(e)