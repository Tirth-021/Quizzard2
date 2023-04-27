import socket 
import random
import threading





class clientthread(threading.Thread):  

    def __init__(self,adr,clt,x):
        #print('Inside class and inside init', cc)
        threading.Thread.__init__(self)
        self.csocket = clt
        self.x =x
        #print(f"connection to {adr} established")
        #self.cc = cc 
    def run(self):
        #print('Inside class and inside run method', self.cc)
        #print(self)
        #print ("Connection from : ", adr)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8')
        while True:
            data2 = self.csocket.recv(1024)
            data2 = data2.decode("utf-8")
            

            # print( y)
            #data1 = self.csocket.recv(1024)
            #data1 = data1.decode("utf-8")
            #k = str(data1)
            if data2 not in self.x:
                print(data2)
            else:
                break
        print("client " +data2+ " disconnected")
        '''print(self.cc)
        cc=self.cc-1
        print(cc)
        return cc 
        break
        print ("Client at ", adr , " disconnected...")'''
class socket_create(threading.Thread):

    def main(self):
        
        port=random.randint(10000,50000)
        print(f'server is running on port: {port}')


        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((socket.gethostname(), port))
        self.s=s #server and client are on same computer #gethostname()
        return port
        #cc = 0
        
    def listing_connections(self):
        x=[]
    #client counter

    #list = [55145,55146]

            
        while 1:
            self.s.listen(1200)
            clt,adr=self.s.accept()
            clt.send(bytes("Welcome to Quizzard","utf-8"))

            data = clt.recv(1024)
            data = data.decode("utf-8")
            x.append(data)
            print("client name: "+data)
            newthread = clientthread(adr, clt ,x)
            newthread.start()
            
            
        
# s=socket_create()
# y=s.main()
# print(y)           
# s=socket_create()
# y=s.main()
# s.listing_connections()            
# z=s1.listen()
# print(z)            
        #cc=cc+1
        #print(cc)  




'''class server1():
    def call(self):
        main()
        
        
s=server1()
s.call()
      '''
        
        
 

    

