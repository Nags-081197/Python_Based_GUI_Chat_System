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

https://pythonprogramming.net/client-chatroom-sockets-tutorial-python-3/

https://pythonprogramming.net/client-chatroom-sockets-tutorial-python-3/

https://www.bogotobogo.com/python/python_network_programming_tcp_client_client_chat_client_chat_client_select.php

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
import tkinter                          ### Importing Tkinter - GUI module
from tkinter import *                   ### Importing everything from tkinter
import json                             ### Importing json header- for json parsing lists & strings
import random                           ### Importing random header to make random choices
import time                             ### Importing time to introduce delay

#########################################################################################################################################################################
""" Function deals username assignment to the client"""
#########################################################################################################################################################################


def connect():
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")                                                                # The message from the server is stored onto variable msg
        if msg == "N":                                                                                          # The msg is checked for "N" that is username is already present condition
            msg_list.insert(tkinter.END, "user name already exists please try another name\n")                  # Inserting a message onto the display region stating the username already exists please select a new username

        elif msg == "Enter Username : ":                                                                        # checking if the message is asking for the user to enter a username
            msg_list.insert(tkinter.END, msg)                                                                   # Inserting a message onto the display region propmting for to enter a username
        else:
            registered.set("YES")                                                                               # setting registered (kind of flag variable) to YES indicating sucessful registeration of the client with a particular username
            if msg[0:7]=="Welcome":
                username_registered.set(msg[8])
            msg_list.insert(tkinter.END, msg)                                                                   # Inserting a message onto the display region stating the Welcome message from the server end
            receive_thread = Thread(target=receive)                                                             # Initialising a new thread to listen to msgs from the server end
            receive_thread.start()                                                                              # starting the initialised thread
            break


#########################################################################################################################################################################################
"""Function deals with the reception of messages from the server, displaying, updating of vector clocks accordingly """
#########################################################################################################################################################################################


def receive():
    username_registered_value = username_registered.get()                                                                                                                                       # This retrieves the username of the currently registered user
    while True:
        msg = client.recv(BUFSIZ)                                                                                                                                                               # The message from the server is stored onto variable msg
        temp_msg = str(msg, "utf8")                                                                                                                                                             # converting it from encoded form to string form and storing it in the variable temp_msg
        if temp_msg[0] != "[" and temp_msg[4:13]!="@@@!!!@@@" :                                                                                                                                 # Checks if the msg starts with "[" since it reserved for different actions and also checks for specific encoding pattern in
            msg_list.insert(tkinter.END, temp_msg)                                                                                                                                              # Inserting the msg onto the display region on the client interface

        elif temp_msg[4:13]=="@@@!!!@@@":                                                                                                                                                       #checking for a specific code pattern
            broke_msg = (temp_msg.split("!@#$%^&*()",6))                                                                                                                                        # splitting the complete temp_msg into 5 at every instance/occurrence of the secret code
            username_tosend = broke_msg[5]                                                                                                                                                      # assigning the usernametosend with split message list's 5th index which is the recipient username
            sender_username = broke_msg[1]                                                                                                                                                      # assigning the senderusername with split message list's 1st index which is the sender username
            Avalue = broke_msg[2]                                                                                                                                                               # vector clock value of client A
            Bvalue = broke_msg[3]                                                                                                                                                               # vector clock value of client B
            Cvalue = broke_msg[4]                                                                                                                                                               # vector clock value of client C
            clientprintmsg = username_tosend +" - Recevied Vector clock value (" + Avalue + "," + Bvalue + "," + Cvalue + ") from " + sender_username                                             # assigning variable with reception message with the vector values and sender and receiver names
            msg_list.insert(tkinter.END, clientprintmsg)                                                                                                                                        # Inserting the msg onto the display region on the client interface


            Afile = str(username_registered_value + 'A' + ".txt")                                                                                                                               # assigning the filename to read the data from
            fh = open(Afile, 'r')                                                                                                                                                               # opening the file to read the message in it
            A_value_to_send = fh.read()                                                                                                                                                         # reading the contents in file onto a string variable
            fh.close()                                                                                                                                                                          # closing the file after reading from it

            Bfile = str(username_registered_value + 'B' + ".txt")                                                                                                                               # assigning the filename to read the data from
            fh = open(Bfile, 'r')                                                                                                                                                               # opening the file to read the message in it
            B_value_to_send = fh.read()                                                                                                                                                         # reading the contents in file onto a string variable
            fh.close()                                                                                                                                                                           # closing the file after reading from it

            Cfile = str(username_registered_value + 'C' + ".txt")                                                                                                                               # assigning the filename to read the data from
            fh = open(Cfile, 'r')                                                                                                                                                               # opening the file to read the message in it
            C_value_to_send = fh.read()                                                                                                                                                         # reading the contents in file onto a string variable
            fh.close()                                                                                                                                                                          # closing the file after reading from it

            if username_registered_value == 'A':                                                                                                                                                # checking for registered user being A

                A_value_incremented = str(int(A_value_to_send)+1)                                                                                                                               #incremented value of previous vector value of A

                if (int(B_value_to_send) > int(broke_msg[3])):                                                                                                                                  # checking is currently received values is lesser than previous
                    final_B_value_to_update = B_value_to_send                                                                                                                                   # assigning previous value of vector only
                elif (int(B_value_to_send) < int(broke_msg[3])):                                                                                                                                # checking is currently received values is greater than previous
                    final_B_value_to_update = broke_msg[3]                                                                                                                                      # assigning new received value of the vector
                else:
                    final_B_value_to_update = B_value_to_send                                                                                                                                   # assigning previous value of vector only

                if (int(C_value_to_send) > int(broke_msg[4])):                                                                                                                                  # checking is currently received values is lesser than previous
                    final_C_value_to_update = C_value_to_send                                                                                                                                   # assigning previous value of vector only
                elif (int(C_value_to_send) < int(broke_msg[4])):                                                                                                                                # checking is currently received values is greater than previous
                    final_C_value_to_update = broke_msg[4]                                                                                                                                      # assigning new received value of the vector
                else:
                    final_C_value_to_update = C_value_to_send                                                                                                                                   # assigning the previous vector value only

                fh = open(Afile, 'w')                                                                                                                                                           # opening the file to write data into the file
                fh.write(A_value_incremented)                                                                                                                                                   # writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                fh = open(Bfile, 'w')                                                                                                                                                           # opening the file to write data into the file
                fh.write(final_B_value_to_update)                                                                                                                                                # writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                fh = open(Cfile, 'w')                                                                                                                                                            # opening the file to write data into the file
                fh.write(final_C_value_to_update)                                                                                                                                                # writing the packed message onto the file
                fh.close()                                                                                                                                                                       # closing the file after writing into it

                tempmsg = "Updated Vector Clock Values (" + str(A_value_incremented) + "," + str(final_B_value_to_update) + "," + str(final_C_value_to_update) + ")"                            # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                            # Inserting the msg onto the display region on the client interface


            elif username_registered_value == 'B':                                                                                                                                              # checking for registered user being B

                B_value_incremented  = str(int(B_value_to_send)+1)                                                                                                                              #incremented value of previous vector value of B

                if (int(C_value_to_send) > int(broke_msg[4])):                                                                                                                                  # checking is currently received values is lesser than previous
                    final_C_value_to_update = C_value_to_send                                                                                                                                   # assigning previous value of vector only
                elif (int(C_value_to_send) < int(broke_msg[4])):                                                                                                                                # checking is currently received values is greater than previous
                    final_C_value_to_update = broke_msg[4]                                                                                                                                      # assigning new received value of the vector
                else:
                    final_C_value_to_update = C_value_to_send                                                                                                                                   # assigning previous value of vector only

                if (int(A_value_to_send) > int(broke_msg[2])):                                                                                                                                  # checking is currently received values is lesser than previous
                    final_A_value_to_update = A_value_to_send                                                                                                                                   # assigning previous value of vector only
                elif (int(A_value_to_send) < int(broke_msg[2])):                                                                                                                                # checking is currently received values is greater than previous
                    final_A_value_to_update = broke_msg[2]                                                                                                                                      # assigning new received value of the vector
                else:
                    final_A_value_to_update = A_value_to_send                                                                                                                                   # assigning previous value of vector only

                fh = open(Afile, 'w')                                                                                                                                                            # opening the file to write data into the file
                fh.write(final_A_value_to_update)                                                                                                                                               # writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                fh = open(Bfile, 'w')                                                                                                                                                           # opening the file to write data into the file
                fh.write(B_value_incremented)                                                                                                                                                   # writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                fh = open(Cfile, 'w')                                                                                                                                                           # opening the file to write data into the file
                fh.write(final_C_value_to_update)                                                                                                                                               # writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                tempmsg = "Updated Vector Clock Values (" + str(final_A_value_to_update) + "," + str(B_value_incremented) + "," + str(final_C_value_to_update) + ")"                            # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                            # Inserting the msg onto the display region on the client interface



            elif username_registered_value == 'C':                                                                                                                                              # checking for registered user being C

                C_value_incremented  = str(int(C_value_to_send)+1)                                                                                                                              #incremented value of previous vector value of C

                if (int(A_value_to_send) > int(broke_msg[2])):                                                                                                                                  # checking is currently received values is lesser than previous
                    final_A_value_to_update = A_value_to_send                                                                                                                                   # assigning previous value of vector only
                elif (int(A_value_to_send) < int(broke_msg[2])):                                                                                                                                # checking is currently received values is greater than previous
                    final_A_value_to_update = broke_msg[2]                                                                                                                                      # assigning new received value of the vector
                else:
                    final_A_value_to_update = A_value_to_send                                                                                                                                   # assigning previous value of vector only

                if (int(B_value_to_send) > int(broke_msg[3])):                                                                                                                                  # checking is currently received values is lesser than previous
                    final_B_value_to_update = B_value_to_send                                                                                                                                   # assigning previous value of vector only
                elif (int(B_value_to_send) < int(broke_msg[3])):                                                                                                                                # checking is currently received values is greater than previous
                    final_B_value_to_update = broke_msg[3]                                                                                                                                      # assigning new received value of the vector
                else:
                    final_B_value_to_update = B_value_to_send                                                                                                                                   # assigning previous value of vector only

                fh = open(Afile, 'w')                                                                                                                                                           # opening the file to write data into the file
                fh.write(final_A_value_to_update)                                                                                                                                               # writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                fh = open(Bfile, 'w')                                                                                                                                                           # opening the file to write data into the file
                fh.write(final_B_value_to_update)                                                                                                                                               #  writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                fh = open(Cfile, 'w')                                                                                                                                                           # opening the file to write data into the file
                fh.write(C_value_incremented)                                                                                                                                                   # writing the packed message onto the file
                fh.close()                                                                                                                                                                      # closing the file after writing into it

                tempmsg = "Updated Vector Clock Values (" + str(final_A_value_to_update) + "," + str(final_B_value_to_update) + "," + str(C_value_incremented) + ")"                            # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                            # Inserting the msg onto the display region on the client interface


##################################################################################################################################################################################################
"""Function deals with the sending of the entered username"""
###################################################################################################################################################################################################

def enter(event=None):                                                                                          # event is passed by binders i.e. by a enter button

    msg = my_msg.get()                                                                                          # Gets and stores the value or string entered in the user input area for username
    my_msg.set("")                                                                                              # Clears the user input field.
    client.send(bytes(msg, "utf8"))                                                                             # send the message stored in msg to the server using the socket object with an encoding

######################################################################################################################################################################################################################################################################################################################
"""Function deals with disconnecting the client from the server"""
######################################################################################################################################################################################################################################################################################################################


def disconnect():
    status = registered.get()                                                                                       # getting the registered flag value onto status variable
    if status == "YES":                                                                                             # checking if status value is "YES" - meaning this is connected/registered user
        exit_msg = '{quit}'                                                                                         # initializing a message {quit}
        client.send(bytes(exit_msg, "utf8"))                                                                        # sending the exit msg to the server with encding
        msg_list.insert(tkinter.END, "YOU DISCONNECTED FROM THE SERVER")                                            # inserting a disconnection message on the screen/display region
        client.close()                                                                                              # Closes the connection through the socket object
        top.quit()                                                                                                  # closes the gui window of the client


################################################################################################################################################################################################################################################################################################################
"""Function deals with starting a thread to get the active clients from the server"""
################################################################################################################################################################################################################################################################################################################

def activeclients():
    get_thread = Thread(target=getactiveclients)                                                                    # initializes a thread for the function get active clients
    get_thread.start()                                                                                              # starts the above initialized thread


##############################################################################################################################################################################################################################################################################################################################
"""Function deals with getting,updating and displaying of vector values"""
###############################################################################################################################################################################################################################################################################################################################


def sendvectorclock():
    global userrandomlist                                                                                               # globale initializing userrandomlist_list

    status = registered.get()                                                                                           # getting the registration of the user and storing the same in status variable
    status_sendvectorclock = sendvectorclock_flag.get()                                                                 # getting the sendvectorclock_flag and storing the same in status variable
    username_registered_value = username_registered.get()

    if status == "YES":                                                                                                 # checking whether the user is a registered user or not that is status variable is "YES"
        if username_registered_value == 'A':                                                                            # checking if registered user is A
            userrandomlist = ['B', 'C']                                                                                 # creating and assigning a list with other two usernames
        elif username_registered_value == 'B':                                                                          # checking if registered user is B
            userrandomlist = ['A', 'C']                                                                                 # creating and assigning a list with other two usernames
        elif username_registered_value == 'C':                                                                          # checking if registered user is B
            userrandomlist = ['A', 'B']                                                                                 # creating and assigning a list with other two usernames

        while(status_sendvectorclock!="NO" and status_sendvectorclock=="YES"):                                          # checking for status flag being set to NO
            Afile = str(username_registered_value+'A'+ ".txt")                                                          # assigning the filename to read the data from
            fh = open(Afile, 'r')                                                                                       # opening the file to read the message in it
            A_value_to_send = fh.read()                                                                                 # reading the contents in file onto a string variable
            fh.close()                                                                                                  # closing the file after reading from it

            Bfile = str(username_registered_value+'B'+ ".txt")                                                          # assigning the filename to read the data from
            fh = open(Bfile, 'r')                                                                                       # opening the file to read the message in it
            B_value_to_send = fh.read()                                                                                 # reading the contents in file onto a string variable
            fh.close()                                                                                                  # closing the file after reading from it

            Cfile = str(username_registered_value+'C'+ ".txt")                                                          # assigning the filename to read the data from
            fh = open(Cfile, 'r')                                                                                       # opening the file to read the message in it
            C_value_to_send = fh.read()                                                                                 # reading the contents in file onto a string variable
            fh.close()                                                                                                  # closing the file after reading from it

            usernametosend = random.choice(userrandomlist)                                                              # selecting a random user from the usernames list

            if username_registered_value == 'A':                                                                        # checking for username being A
                final_A_value_to_send = str(int(A_value_to_send)+1)                                                     # incrementing the previous vector value for the user by one

                fh = open(Afile, 'w')                                                                                                                                                                                                                                                               # opening the file to write data into the file
                fh.write(final_A_value_to_send)                                                                                                                                                                                                                                                      # writing the packed message onto the file
                fh.close()                                                                                                                                                                                                                                                                          # closing the file after writing into it

                temp = "@@@!!!@@@" + "!@#$%^&*()" + str(username_registered_value) + "!@#$%^&*()" + str(final_A_value_to_send) + "!@#$%^&*()" + str(B_value_to_send) + "!@#$%^&*()" + str(C_value_to_send) + "!@#$%^&*()" + str(usernametosend) + "!@#$%^&*()"                                      # manual encoding of vector values,sender, receiver data with a piece of redundant code
                tempmsg = "Sending - " + str(username_registered_value) + "'s Vector Clock Values (" + str(final_A_value_to_send) + "," + str(B_value_to_send) + "," + str(C_value_to_send) + ") to " + str(usernametosend)                                                                           # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                                                                                                                                # Inserting the msg onto the display region on the client interface
                tempmsg = "Updated Vector Clock Values (" + str(final_A_value_to_send) + "," + str(B_value_to_send) + "," + str(C_value_to_send) + ")"                                                                                                                                              # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                                                                                                                                # Inserting the msg onto the display region on the client interface
                client.send(bytes(temp, "utf8"))                                                                                                                                                                                                                                                    # sending the packaged data to the server

            elif username_registered_value == 'B':                                                                                                                                                                                                                                                  # checking for username being B
                final_B_value_to_send = str(int(B_value_to_send)+1)                                                                                                                                                                                                                                 # incrementing the previous vector value for the user by one

                fh = open(Bfile, 'w')                                                                                                                                                                                                                                                               # opening the file to write data into the file
                fh.write(final_B_value_to_send)                                                                                                                                                                                                                                                     # writing the packed message onto the file
                fh.close()                                                                                                                                                                                                                                                                          # closing the file after writing into it

                temp = "@@@!!!@@@" + "!@#$%^&*()" + str(username_registered_value) + "!@#$%^&*()" + str(A_value_to_send) + "!@#$%^&*()" + str(final_B_value_to_send) + "!@#$%^&*()" + str(C_value_to_send) + "!@#$%^&*()" + str(usernametosend) + "!@#$%^&*()"                                      # manual encoding of vector values,sender, receiver data with a piece of redundant code
                tempmsg = "Sending - " + str(username_registered_value) + "'s Vector Clock Values (" + str(A_value_to_send) + "," + str(final_B_value_to_send) + "," + str(C_value_to_send) + ") to " + str(usernametosend)                                                                           # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                                                                                                                                # Inserting the msg onto the display region on the client interface
                tempmsg = "Updated Vector Clock Values (" + str(A_value_to_send) + "," + str(final_B_value_to_send) + "," + str(C_value_to_send) + ")"                                                                                                                                              # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                                                                                                                                 # Inserting the msg onto the display region on the client interface
                client.send(bytes(temp, "utf8"))                                                                                                                                                                                                                                                    # sending the packaged data to the server


            elif username_registered_value == 'C':                                                                                                                                                                                                                                                  # checking for username being B
                final_C_value_to_send = str(int(C_value_to_send)+1)                                                                                                                                                                                                                                 # incrementing the previous vector value for the user by one

                fh = open(Cfile, 'w')                                                                                                                                                                                                                                                                # opening the file to write data into the file
                fh.write(final_C_value_to_send)                                                                                                                                                                                                                                                     # writing the packed message onto the file
                fh.close()                                                                                                                                                                                                                                                                          # closing the file after writing into it

                temp = "@@@!!!@@@" + "!@#$%^&*()" + str(username_registered_value) + "!@#$%^&*()" + str(A_value_to_send) + "!@#$%^&*()" + str(B_value_to_send) + "!@#$%^&*()" + str(final_C_value_to_send) + "!@#$%^&*()" + str(usernametosend) + "!@#$%^&*()"                                      # manual encoding of vector values,sender, receiver data with a piece of redundant code
                tempmsg = "Sending - " + str(username_registered_value) + "'s Vector Clock Values (" + str(A_value_to_send) + "," + str(B_value_to_send) + "," + str(final_C_value_to_send) + ") to " + str(usernametosend)                                                                           # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                                                                                                                                # Inserting the msg onto the display region on the client interface
                tempmsg = "Updated Vector Clock Values (" + str(A_value_to_send) + "," + str(B_value_to_send) + "," + str(final_C_value_to_send) + ")"                                                                                                                                              # Message showing the currently updated values of the vectors
                msg_list.insert(tkinter.END,tempmsg)                                                                                                                                                                                                                                                # Inserting the msg onto the display region on the client interface
                client.send(bytes(temp, "utf8"))                                                                                                                                                                                                                                                    # sending the packaged data to the server

            time.sleep(random.randint(2,10))                                                                                                                                                                                                                                                        # giving a delay randomly between 2 to 9 seconds
            status_sendvectorclock = sendvectorclock_flag.get()                                                                                                                                                                                                                                     # getting the sendvectorclock_flag and storing the same in status variable
        exit(0)                                                                                                                                                                                                                                                                                     # to kill the thread and exit
    exit(0)





################################################################################################################################################################################################################################################################################################################
"""Function deals with starting a thread to sendvectorclock """
################################################################################################################################################################################################################################################################################################################

def startmessaging():
    sendvectorclock_flag.set("YES")
    get_thread_all = Thread(target=sendvectorclock)                                                                     # initializes a thread for the function sendvectorclock
    get_thread_all.start()                                                                                              # starts the above initialized thread

################################################################################################################################################################################################################################################################################################################
"""Function deals with stopping the messaging (vector clock exchange) between clients to sendvectorclock """
################################################################################################################################################################################################################################################################################################################

def stopmessaging():
    sendvectorclock_flag.set("NO")                                                                                      # setting the value of the sendvectorclock flag to "NO" to end the exchange of messages

##############################################################################################################################################################################################################################################################################################################################
"""Funcation deals with getting a list of all active users from the server """
###############################################################################################################################################################################################################################################################################################################################


def getactiveclients():
    global activeclients_list                                                                                           # globale initializing activeclients_list

    status = registered.get()                                                                                           # getting the registration of the user and storing the same in status variable
    if status == "YES":                                                                                                 # checking whether the user is a registered user or not that is status variable is "YES"
        activeclients_msg = 'active_clients'                                                                            # initializing activeclients_msg to string "active_clients"  which is reserved keyword for this program
        client.send(bytes(activeclients_msg, "utf8"))                                                                   # sending the activeclients_msg to the server
        jsonstring = client.recv(BUFSIZ).decode("utf8")                                                                 # waiting for the response message from the server which will be a string form of a list containing all the active users connected to the client

        if jsonstring[0] == "[":                                                                                        # checking whether it a string form of the list of the active clients

            activeclients_list = json.loads(jsonstring)                                                                 # converting back the string to list using the json.loads fucntion
            if bool(activeclients_list):                                                                                # checking whther the list is empty or not
                users.delete(0, tkinter.END)                                                                            # deleting all the messages inserted in the active users listbox display unit
                users.insert(tkinter.END, "Active clients\n")                                                           # inserting message Active clients into the user listbox
                for x in range(len(activeclients_list)):                                                                # traversing for the total number of users present in the list
                    users.insert(tkinter.END, "%s\n" % activeclients_list[x])                                           # inserting each username onto the zctive userlist display region

            else:                                                                                                       # when the active clients list is empty
                users.delete(0, tkinter.END)                                                                            # clearing all the previous inserted messages on the users listbox
                users.insert(tkinter.END, "No active clients\n")                                                        # insert a msg No active clients onto the users listbox in the frame

        else:                                                                                                           # if the received msg is not a list of active clients
            msg_list.insert(tkinter.END, jsonstring)                                                                    # Inserting the message onto the message listbox



################################################################################################################################################################################################################
""" Declaration  of global variables"""
################################################################################################################################################################################################################3


global activeclients_list                       # used to store the active client users got from the server
global status                                   # used to mark the registration status of the user



################################################################################################################################################################################################################
""" Client GUI Window setup """
################################################################################################################################################################################################################3



top = tkinter.Tk()                                                                                                      # initializing a tkinter object as top
top.title("Client_2")                                                                                                   # naming the client window/frame
my_msg = tkinter.StringVar()                                                                                            # used to store the value from the username entry field - tkinter string variable object
my_msg.set("")                                                                                                          # clearing the entry field after the username entry

my_msg_entered = tkinter.StringVar()                                                                                    # variable to store specific message to the users
my_msg_entered.set("")                                                                                                  # setting the variable to ""

registered = StringVar(master=top)                                                                                      # variable used as a flag to inidicate the status of registration of a particular username
registered.set("NO")                                                                                                    # setting the variable to "NO" initially

username_registered = StringVar(master=top)                                                                             # variable used to store username_registered
username_registered.set("NONE")                                                                                         # setting the variable to "NONE" initially

sendvectorclock_flag = StringVar(master=top)                                                                            # variable used as a flag to indicate the status of sendvectorclock
sendvectorclock_flag.set("NO")                                                                                          # setting the variable to "NO" initially

################################################################################################################################################################################################################
""" CLIENT GUI SETUP"""
################################################################################################################################################################################################################3

messages_frame = tkinter.Frame(top)                                                                                     #initializing the tkinter frame to display everything

scrollbar = tkinter.Scrollbar(messages_frame)                                                                           # To scroll about the view screen or display
msg_list = tkinter.Listbox(messages_frame, height=25, width=70, yscrollcommand=scrollbar)                               # a listbox object from tkinter to showcase the received messages
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)                                                                      # packing the scrollbar onto the right of screen
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)                                                                     # positioning and packing of the msg listbox onto the frame
msg_list.pack()                                                                                                         # packing message list box
users = tkinter.Listbox(messages_frame, height=25, width=20)                                                            # a listbox object to display the active users list
users.pack(side=tkinter.RIGHT)                                                                                          # packing os the listbox for active users list
messages_frame.pack()                                                                                                   # pack all the items in the main display frame message frame
users.insert(tkinter.END, "No active clients\n")                                                                        # inserting and initializing the active users list box

entry_field = tkinter.Entry(top, textvariable=my_msg)                                                                   # creating an entry field for the username entryy
entry_field.bind("<Return>", enter)                                                                                     # binding the entry field with a entry function
entry_field.pack()                                                                                                      # pakcing the entry field into the main gui frame

enter_button = tkinter.Button(top, text="Enter", command=enter)                                                         # entry button used to trigger the enter function to send the username to server
enter_button.pack()                                                                                                     # packing the enter button onto the main gui frame

disconnect_button = tkinter.Button(top, text="Disconnect", command=disconnect)                                          # disconnect button used to trigger disconnect function to disconnect the client from the erver
disconnect_button.pack()                                                                                                # packing the disconnect button onto the main gui frame

activeclients_button = tkinter.Button(top, text="Get Active Clients", command=activeclients)                            # activeclients button used to traigger the function activeclients to get the list active users from the server and display the username selection window depending on the messaging iption selected
activeclients_button.pack()                                                                                             # packing the activeclients button onto the main gui frame

startmessaging_button = tkinter.Button(top, text="Start Sending Vector Clock Values", command=startmessaging)           # start messaging button used to trigger the function startmessaging to start the exchange of messages(vector clocks)
startmessaging_button.pack()                                                                                            # packing the start messaging button onto the main gui frame

stopmessaging_button = tkinter.Button(top, text="Stop Sending Vector Clock Values", command=stopmessaging)              # stop messaging button used to trigger the function startmessaging to stopt the exchange of messages(vector clocks)
stopmessaging_button.pack()                                                                                             # packing the stop messaging button onto the main gui frame


################################################################################################################################################################################################################
""" SOCKET Setup"""
################################################################################################################################################################################################################3


host = "127.0.0.1"                                                              # host IP address for the client to connect to
port = 12345                                                                    # host port number to communicate with the server
BUFSIZ = 1024                                                                   # buffer to temporarily store msgs from the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      # creating a client socket object
client.connect((host, port))                                                    # Trying to establish connection with the server using the above mentioned credentials
connect_thread = Thread(target=connect)                                         # initializing a thread to connect with the server and register a username
connect_thread.start()                                                          # starting the above mentioned thread
tkinter.mainloop()                                                              # Starts client GUI module as main loop



################################################################################################################################################################################################################
""" END OF CLIENT CODE"""
################################################################################################################################################################################################################3
