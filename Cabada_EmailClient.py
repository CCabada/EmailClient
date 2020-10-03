#CS5313: Computer Networks		Fall 2020
#Instructor: Dr. Deepak Tosh 		Date: 09/18/2020
#Carlos Cabada

from socket import *
import sys
import re
import time

def check(email):
    # Regular expression for validating an Email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False


def connect_server(server, port, socket):
    try:
        # connecting to the server
        socket.connect((server, port))
        print("Socket successfully connected")
        
    except socket.gaierror:
        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()


def helo(server, socket):
    try:
        helo = 'HELO '+server+'\r\n'
        # sending helo command to start SMTP conversation with the server
        socket.send(helo.encode())
        print("Sent the HELO Command Successfully")
        server_response = socket.recv(1024)
        print(server_response.decode())


    except socket.gaierror:
        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()


def email(sender, recepient, socket):
    send = 'mail from: '+sender+'\r\n'
    receive = 'rcpt to: '+recepient+'\r\n'
    data = 'DATA\r\n'
    period = '\r\n.\r\n'
    try:
        ####################################################################################
        #Sends the sender's email
        time.sleep(3)
        socket.send(send.encode())
        server_response = socket.recv(1024)
        print(server_response.decode())
        time.sleep(3)
        ####################################################################################
        # Sends the receiver's email
        socket.send(receive.encode())
        server_response = socket.recv(1024)
        print(server_response.decode())
        time.sleep(3)
        ####################################################################################
        # Sends the "DATA" to the server
        socket.send(data.encode())
        server_response = socket.recv(1024)
        print(server_response.decode())
        ####################################################################################
        # Sends the Subject line plus the email to the server
        time.sleep(3)
        subjectLine = "SUBJECT: "+input("What is the subject line?")+"\r\n\r\n"
        email_body = input("What is the Email body?")
        email = subjectLine + email_body
        socket.send(email.encode())
        server_response = socket.recv(1024)
        print(server_response.decode())

        ####################################################################################
        # Sends the terminator character, ".", to the server

        time.sleep(3)
        socket.send(period.encode())
        server_response = socket.recv(1024)
        print(server_response.decode())

    except socket.gaierror:
        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()



def main():
    # Utep's smtp server
    smtp_server = "smtp.utep.edu"
    port = 25
    #email_format = False


    #while (email_format == False):
    #    sender_email = input("What is the sender's email? \n")
    #    if (check(sender_email)):
    #        email_format = True
    #    recepient_email = input("What is the recepient's email? \n")
    #    if (check(recepient_email)):
    #        email_format = True
    sender_email = input("What is the sender's email? \r\n")

    recepient_email = input("What is the recepient's email? \r\n")

    new_socket = socket(AF_INET, SOCK_STREAM)



    # connecting to the server
    connect_server(smtp_server, port, new_socket)
    # initiates 3 way handshake
    helo(smtp_server, new_socket)
    email(sender_email, recepient_email, new_socket)

    new_socket.close()





main()

