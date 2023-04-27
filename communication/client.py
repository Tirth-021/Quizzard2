import socket
import names

port = int(input("Enter room number:"))

name=names.get_full_name()
print('Hi,',name)
# Ren. Name
# 123456
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), port))
c.send(bytes(name,"utf-8"))


msg=c.recv(1024)
complete_info = msg.decode("utf-8")
print(complete_info)


while 1:
    msg1=input('Type "exit" for exit else Enter your message:')
    #print(msg1)
    x= name+" message: "+msg1
    #y= "client "+name+" is disconnected:"
    #print(c.send(bytes(name,"utf-8")),'----error----')

    if msg1 == 'exit':
        #print('Inside If and send and break')
        #print('---',name,'--')
        c.send(bytes(name,"utf-8"))
        break   
    else:
        #print('Inside else')
        c.send(bytes(x,"utf-8"))    






    

