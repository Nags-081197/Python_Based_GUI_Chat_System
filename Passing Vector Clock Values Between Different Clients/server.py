"""AUTHOR : NAGASHEKAR ANANDA"""
"""UNIVERSITY OF TEXAS AT ARLINGTON"""

##########################################################################################################################################################################
"""----------------------------------------References:-------------------------------------------------------------------------------------------------"""
##########################################################################################################################################################################
"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------Following videos/links/document links include Sockets, Client-Server Model, Multi-threading, Chat room, Broadcast messages, Multiclient chat system ---------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


https://www.geeksforgeeks.org/simple-chat-room-using-python/

https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170

https://pythontips.com/2013/08/06/python-socket-network-programming/

https://github.com/attreyabhatt/Reverse-Shell/tree/master/Multi_Client%20(%20ReverseShell%20v2)

https://pythonprogramming.net/sockets-tutorial-python-3/

https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/

https://pythonprogramming.net/client-chatroom-sockets-tutorial-python-3/

https://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php

https://github.com/KetanSingh11/SimpleChatApp

https://github.com/naveensn/Naveen_GitRepo/commit/084a277eb29f46f122e17a43ee03074c5478c428

https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

https://www.geeksforgeeks.org/python-string-split/



-----------------------------------------------------------------------------------------------------------------------------------------------------------
Following videos/links/document links include tutorials, code snippets, widgets, buttons, multiple frames, syntax for TKINTER (GUI MODULE) Using Python
-----------------------------------------------------------------------------------------------------------------------------------------------------------


https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/

https://mail.python.org/pipermail/tutor/2009-October/072145.html

https://stackoverflow.com/questions/6919596/tkinter-radio-buttons-does-not-work-inside-function

https://stackoverflow.com/questions/35660342/radio-button-values-in-python-tkinter

https://www.python-course.eu/tkinter_radiobuttons.php

https://stackoverflow.com/questions/47386185/how-to-create-multiple-checkbox-in-loop-using-tkinter

https://stackoverflow.com/questions/15306631/how-do-i-create-child-windows-with-python-tkinter

https://www.youtube.com/watch?v=IB6VkXJVf0Y

https://www.youtube.com/watch?v=qWnE-yp6wzU&t=163s

https://www.youtube.com/watch?v=_lSNIrR1nZU



"""
##########################################################################################################################################################################################
"""------------------------------------------------END OF REFERENCES---------------------------------------------------------------------------"""
##########################################################################################################################################################################################


##########################################################################################################################################################################################
"""IMPORTING HEADER PACKAGES"""
##########################################################################################################################################################################################


import socket                           ### Importing socket header file to get socket objects & connecting programs
import threading                        ### Importing threading header file to get multi-threading  & create different execution flows
from threading import Thread            ### Aliasing the threading header as Thread
import tkinter as tk                    ### Tkinter - GUI module - aliasing tkinter as tk
import json                             ### Importing json header- for json parsing lists & strings



#########################################################################################################################################################################
""" Function - to listen incoming connections and pass it onto the connection accepting function"""
#########################################################################################################################################################################

def econnection():
    while True:
        s.listen(5)                                                                 # Socket object (server) listens to incoming connections
        connect_thread = threading.Thread(target=accept_incoming_connections)       # Creating a new thread for accepting to the incoming connections to the server
        connect_thread.start()                                                      # Starting the thread created above
        connect_thread.join()                                                       # To Join the forked thread to the main thread
        s.close()                                                                   # To close the socket object from listening to the incoming connections


##########################################################################################################################################################################
"""Function to accept incoming connections on the server end"""
##########################################################################################################################################################################


def accept_incoming_connections():
    while True:
        client, client_address = s.accept()                                         # Assigning client & client address variable with client and client address from the incoming connection through the socket object "s"
        list_of_clients.append(client)                                              # Appending/Adding client to the list of clients
        msg.insert(tk.END, "NEW CONNECTION ESTABLISHED !!")                         # inserting a message onto the message display section for a connection establishment
        client.send(bytes("Enter Username : ", "utf8"))                             # Send a message prompting for a user name from the user at the client side
        addresses[client] = client_address                                          # Adding client address from the socket object to the addresses list - to store as a copy of all the addresses
        Thread(target=handle_client, args=(client, msg)).start()                    # Forking a thread to receive the incoming input of the username and handling of the connection


##############################################################################################################################################################################
""" Function to handle the connections with the username from the client side """
##############################################################################################################################################################################



def handle_client(client, msg):                                                                                 # function takes client object and msg frame object for displaying messages

    while True:                                                                                                 # infinite traversal of the following statements
        user_name = client.recv(BUFSIZ).decode("utf8")                                                          # Waits and receives the username entered and pushed onto the server from client/user end

        if user_name in user_names:                                                                             # checking whether the username is already used by any other connected clients on the server
            client.send("N".encode("utf8"))                                                                     # server sends "N" to indicate that the client that this username is already taken by a different client


        elif user_name !={quit} and not user_name.isspace() and user_name !="active_clients":                   # checking whether the username is not {quit}, " " -just a space or "active_clients" as these are reserved for other funtionalities in the system
            msg.insert(tk.END, user_name + " connected\n")                                                      # inserting a messaging stating that the client with a certain username has successfully connected to the server
            user_names.add(user_name)                                                                           # adding the same username given by the client to the set user_names
            concurrent_usernames.add(user_name)                                                                 # adding the same username given by the client to the set concurrent_user_names
            concurrent_usernames_list = list(concurrent_usernames)                                              # coverting the set concurrent usernames to a list for data traversal in the upcoming conditions checks
            clients[client] = user_name                                                                         # associating the client address, port no. etc with the user provided username
            welcome = 'Welcome %s ' % user_name + "\n"                                                          # creating a welcome message with the username to send to the client
            client.send(bytes(welcome, "utf8"))                                                                 # sending a welcome message to the recently connected client/user
            users.delete(0, tk.END)                                                                             # clearing the active user display region
            users.insert(tk.END, "Active clients\n")                                                            # inserting a text - "Active clients" - acts a heading or label for the region
            concurrent_users.delete(0, tk.END)                                                                  # clearing the concurrent user logs display region
            concurrent_users.insert(tk.END, "Cumulative User(s) Log \n")                                         # inserting a text - "Active clients" - acts a heading or label for the region
            for x in range(len(concurrent_usernames_list)):                                                     # traversing for the total number of users in the concurrent users log
                concurrent_users.insert(tk.END, "%s\n"%concurrent_usernames_list[x])                            # inserting the names of the concurrent users on the display region
            for client in clients:                                                                              # traversing for the total number of active clients connected to the server
                users.insert(tk.END, " " + str(clients[client]) + "\n")                                         # inserting the names of the active users usernames on to the display region
            try:
                client.send("Now you can start your Chat !!\n".encode("utf8"))                                                              # Sending a message to the client that they can start the chat now
                connection_notification = ' joined the Chat \n'                                                                             # Creating a connection notification message
                connection_notification_thread = threading.Thread(target=send_to_all, args=(connection_notification, user_name))            # assigning a thread to send the connection notification msg to all the users/clients using the send_to_all function
                connection_notification_thread.start()                                                                                      # starting the thread to do the above operation
                messaging_thread = threading.Thread(target=messaging, args=(client, user_name))                                             # assigning a new thread to handle the messages from the client end
                messaging_thread.start()                                                                                                    # starting the thread to do the above operation
                break
            except socket.error:                                                                                                            # expecting a socket error from the socket object created
                msg.insert(tk.END, "connection error : make sure server is running, IP and port# are correct\n")                            # putting up a message on the msg display region stating an error in the socket



##########################################################################################################################################################################################################################################################################################
""" Function deals with the messaged from the client and responses for it"""
##########################################################################################################################################################################################################################################################################################


def messaging(client, user_name):                                                                                                      # the function takes the forked client and its username as parameters
    while True:
        message = client.recv(BUFSIZ)                                                                                                  # waits to receive message from the intended client and us stored a variable called message
        temp_msg = str(message, "utf8")                                                                                                # decoding the message to a temporary variable

        if temp_msg[0:9]=="@@@!!!@@@":                                                                                                                                  # checking for the first 10 elements to be a specific code
            broke_msg = (temp_msg.split("!@#$%^&*()",6))                                                                                                                # splitting the complete temp_msg into 5 at every instance/occurrence of the secret code
            username_tosend = broke_msg[5]                                                                                                                              # assigning the usernametosend with split message list's 4th index which is the recipient username
            sender_username = broke_msg[1]                                                                                                                              # assigning the senderusername with split message list's 1st index which is the sender username
            Avalue = broke_msg[2]                                                                                                                                       # vector clock value of client A
            Bvalue = broke_msg[3]                                                                                                                                       # vector clock value of client B
            Cvalue = broke_msg[4]                                                                                                                                       # vector clock value of client C

            serverprintmsg = sender_username+" Sending Vector clock value ("+Avalue+","+Bvalue+","+Cvalue+") to "+username_tosend                                       # creating a sending or transmitting message consisting of the sender, receiver and the vector clock
            msg.insert(tk.END, serverprintmsg)                                                                                                                          # insert the same msg in msg display region
            clientaddresstosend = (list(clients.keys())[list(clients.values()).index(username_tosend)])                                                                 # storing the key value(address value) associated with the username - recipient address
            send_to_unicast(temp_msg, clientaddresstosend,user_name)                                                                                                    # calling the send_to_unicast function and passing msgtouser, the recipient client address & the sender's username

        elif (message != bytes("{quit}", "utf8")) and (user_name in user_names) and (message!=bytes("active_clients","utf8")and(message!=bytes("@@@!!!@@@"))):          # checking whther its not a quit msg and active_clients and the sender is in the active clients list
            send_to_all(message, user_name + ":")                                                                                                                       # calling the sendtoall function and passing the message and the username to broadcast the message
            msg.insert(tk.END, message)                                                                                                                                 # insert the same msg in msg display region

        elif message == bytes("active_clients","utf8"):                                                                                 # checking if it a active_clients message
            listtosend = list(user_names)                                                                                               # coverting the usernames set into a list to pass it onto the client
            active_usernames_list = json.dumps(listtosend)                                                                              # coverting the list into a string using the json.dumps
            client.send(bytes(active_usernames_list, "utf8"))                                                                           # sending the string containing the list of active users is then sent to requested client


        elif message == bytes("{quit}","utf8"):                                                                                         # checking of quit msg
            closure_msg = " Left the Chat !! \n"                                                                                        # assigning a notifier string closure msg
            msg.insert(tk.END, user_name + " has Disconnected\n")                                                                       # inserting onto the msg region on the server gui about the clients disconnection
            user_names.remove(user_name)                                                                                                # removing the same user from the usernmaes set
            del clients[client]                                                                                                         # deleting the record (client address) of the client requesting for disconnection
            if bool(clients):                                                                                                           # checking if the active clients list is empty or not
                users.delete(0, tk.END)                                                                                                 # emptying the active clients display region
                users.insert(tk.END, "Active clients\n")                                                                                # inserting active clients as a heading to the reagion
                for client in clients:                                                                                                  # traversing each client present in the clients list
                    users.insert(tk.END, " " + str(clients[client]) + "\n")                                                             # inserting each active client present in the list other below the other
            else:                                                                                                                       # if no users present in the active clients list
                users.delete(0, tk.END)                                                                                                 # emptying the active clients display region
                users.insert(tk.END, "No active clients\n")                                                                             # inserting the message no active clients onto the active clients display region
            send_to_all(closure_msg,user_name)                                                                                          # calling send to all to broadcast the message of disconnection of this particular user to all other active clients present on the system

            exit(0)                                                                                                                     # ending and killing the thread/ process


#########################################################################################################################################################################################################################################
"""function deals with broadcasting of messages ( notifiers ) (system to ALL users) notifications broadcast  """
#########################################################################################################################################################################################################################################


def send_to_all(msg,username):                                                                                  # the function accepts a message to be sent and the username of the user who is trying to send the message
    clientaddressestosend_list = []                                                                             # list used to store the username to client address mapping for each username
    for x in (user_names):                                                                                      # traversing through all the active usernames presently connected to the server
        item_to_append = (list(clients.keys())[list(clients.values()).index(x)])                                # storing the key value(address value) associated with each username
        clientaddressestosend_list.append(item_to_append)                                                       # adding each address values to the list
    finalmsg = str(username+" : "+msg)                                                                               # creating a final message with username and message passed to the function
    for client in clientaddressestosend_list:                                                                   # traversing each client address in the list
        client.send(bytes((finalmsg), "utf8"))                                                                  # send the message to all the users present in the list with the senders username



########################################################################################################################################################################################################################################
"""function deals with sending of message to a particular recipient (one-to-one) UNICAST"""
########################################################################################################################################################################################################################################


def send_to_unicast(msg,client_add,user_name):                                                                  # the fucntion takes the message, recepient client address & senders username as parameter
        client_add.send(bytes((user_name+" : "+msg),"utf8"))                                                    # send the username with the message to the intended recepient


##############################################################################################################################################
"""SOCKETS SETUP"""
##############################################################################################################################################


list_of_clients = []                # list to hold all the client addresses, socket number
s = socket.socket()                 # Creating a socket object "s"
host = "127.0.0.1"                  # Setting HOST IP to the following value - for the clients to connect to
port = 12345                        # Initializing the port no. to the following value - for the clients to connect to
s.bind((host, port))                # packing/binding of socket object "s" with the above mentioned port no. and host ip address
s.listen(5)                         # Socket object (server) listens to incoming connections


#############################################################################################################################################
"""variable initialization"""
#############################################################################################################################################


clients = {}                            # creating an empty dictionary to store the corresponding client username with the client address
addresses = {}                          # creating an empty dictionary to store address values which will be taken up by the server
user_names = set()                      # creating a set to store the active usernames connected to the server - to check the active connectivity of the client and to redirect the messaged from other clients
concurrent_usernames = set()            # creating a set to store the concurrent/log of usernames which have been used to connect to the server - to display
BUFSIZ = 1024                           # creating a buffer size variable and initializing it, which will be used to temporaryly store messages recevied from the client


##############################################################################################################################################
"""GUI SETUP"""
##############################################################################################################################################

window = tk.Tk()                                                                    # Creating a tkinter object
window.title("Server")                                                              # Naming the window or the screen
window.geometry("750x600")                                                          # Setting the dimensions of the screen (width x height) format
frame = tk.Frame(window)                                                            # Creating a frame(screen) to display

scrollbar = tk.Scrollbar(frame)                                                     # Scroll button initialization for navigating the messages
msg = tk.Listbox(frame, height=50, width=70, yscrollcommand=scrollbar)              # Creating a message display region (type listbox) to output the messages
msg.pack(side=tk.LEFT, fill=tk.BOTH)                                                # Positioning of the message display region on the main window
msg.pack()                                                                          # Actual binding/packing of the message display region onto the main window
users = tk.Listbox(frame, height=50, width=25)                                      # Creating a active users list display region to output the active users
users.pack(side=tk.RIGHT)                                                           # Positioning and packing of the active users display region
concurrent_users = tk.Listbox(frame, height=50, width=25)                           # Creating a concurrent users list/ user log  display region to output the active users
concurrent_users.pack(side=tk.LEFT)                                                 # Positioning and packing of the users log display region
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)                                            # Positioning and packing of the scroll button the right
frame.pack()                                                                        # Packing/binding of the whole frame on the main window

users.insert(tk.END, "No active clients\n")                                         # Inserting an offset message on to the active users list display region
concurrent_users.insert(tk.END, "No User(s) Logs\n")                                # Inserting an offset message on to the users log/ concurrent users list display region
msg.insert(tk.END, "Server started...\n")                                           # Inserting an offset message on to the message display region

threading.Thread(target=econnection).start()                                        # Forking a new thread for listening to the incoming connections to the server
tk.mainloop()                                                                       # Starting the GUI mainloop function to start the display on the screen



################################################################################################################################################################################################################
""" END OF SERVER CODE """
################################################################################################################################################################################################################3
