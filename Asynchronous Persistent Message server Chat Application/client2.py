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
            msg_list.insert(tkinter.END, msg)                                                                   # Inserting a message onto the display region stating the Welcome message from the server end
            receive_thread = Thread(target=receive)                                                             # Initialising a new thread to listen to msgs from the server end
            receive_thread.start()                                                                              # starting the initialised thread
            break


#########################################################################################################################################################################################
"""Function deals with the reception of messages from the server & displaying """
#########################################################################################################################################################################################


def receive():
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")                                                                # The message from the server is stored onto variable msg
        if msg[0] != "[":                                                                                       # Checks if the msg starts with "[" since it reserved for different actions
            msg_list.insert(tkinter.END, msg+"\n")                                                                   # Inserting the msg onto the display region on the client interface


##################################################################################################################################################################################################
"""Function deals with the sending of the entered username"""
###################################################################################################################################################################################################


def enter(event=None):                                                                                          # event is passed by binders i.e. by a enter button

    msg = my_msg.get()                                                                                          # Gets and stores the value or string entered in the user input area for username
    my_msg.set("")                                                                                              # Clears the user input field.
    client.send(bytes(msg, "utf8"))                                                                             # send the message stored in msg to the server using the socket object with an encoding


##############################################################################################################################################################################################################
"""Function deals with the setting up of a message entry window to enter a brief message to the other users"""
##############################################################################################################################################################################################################


def message_to_send(event=None):                                                                                                     # event is passed by binders i.e. by a enter message send button
    status = registered.get()                                                                                                        # retrieving the registered flag onto the status variable
    if status == "YES":                                                                                                              # checking if the status is "YES" or not -  meaning this is connected/registered user or not
        global message_to_send_frame, send_message                                                                                   # gloabal delcaration of variables

        message_to_send_frame = tkinter.Toplevel(top)                                                                                # creating a child window from the main GUI window
        message_to_send_frame.geometry("200x100")                                                                                    # setting the dimensions of the child window (width x height)
        message_to_send_frame.title(" Client 2 Message Tab ")                                                                        # Title for the child window
        message_to_send_field = tkinter.Entry(message_to_send_frame, textvariable=my_msg_entered)                                    # creating an entry field and associating it with textvariable my_msg_entered
        message_to_send_field.bind("<Return>", send_message_to_specific_user)                                                        # binding the above mentioned entry field with a funtion calles send_message to specific user
        message_to_send_field.pack()                                                                                                 # packing or binding everything onto the child window/frame
        send_message = tkinter.Button(message_to_send_frame, text="Send Message", command=send_message_to_specific_user)             # Creating a button to trigger the function send_message_to_specific_user
        send_message.pack()                                                                                                          # packing the button onto the button


##########################################################################################################################################################################################################################
"""Function deals with Message packing for different types of messaging options - unicast, multicast, broadcast depending on the selection"""
##########################################################################################################################################################################################################################


def send_message_to_specific_user():
    msg = my_msg_entered.get()                                                                                                                      # Gets the message from the user entry field
    my_msg_entered.set("")                                                                                                                          # Clears input user entry field
    msg_len = len(msg)                                                                                                                              # getting the length of the entered message
    msg_len_str = str(msg_len)                                                                                                                      # converting the int of the msg_length into str for concatination with the msg entered by the user
    if msg_len == 0 or msg == " ":                                                                                                                  # chekcing if the enetred message is empty or is of zero length
        msg_list.insert(tkinter.END, "PLEASE ENTER A MESSAGE !!")                                                                                   # inserting a message onto the display region prompting the user to enter the message before sending message

    else:                                                                                                                                           # if the msg length is greater than zero and message length is greater than 0
        if selected == "1":                                                                                                                         # checking if the selected variable is "1" meaning it is a unicast message
            temp = "!@#$%^&*()" + selected + "!@#$%^&*()" + msg_len_str + "!@#$%^&*()" + msg + "!@#$%^&*()" + unicast_selection + "!@#$%^&*()"      # manual encoding of selected variable,msg,msglen,unicast selection with a piece of redundant code
            client.send(bytes(temp, "utf8"))                                                                                                        # sending the above packed str stored in temp variable to the server over the socket

        elif selected == "2":                                                                                                                       # checking if the selected variable is "2" meaning it is a multicast message
            mlist = json.dumps(multicast_list)                                                                                                      # converting the multicast usernames list into a str for the manual encoding
            temp = "!@#$%^&*()" + selected + "!@#$%^&*()" + msg_len_str + "!@#$%^&*()" + msg + "!@#$%^&*()" + mlist + "!@#$%^&*()"                  # manual encoding of selected variable,msg,msglen,multicast selection list with a piece of redundant code
            client.send(bytes(temp, "utf8"))                                                                                                        # sending the above packed str stored in temp variable to the server over the socket

        elif selected == "3":                                                                                                                        # checking if the selected variable is "3" meaning it is a broadcast message
            temp = "!@#$%^&*()" + selected + "!@#$%^&*()" + msg_len_str + "!@#$%^&*()" + msg + "!@#$%^&*()" + "ALL" + "!@#$%^&*()"                   # manual encoding of selected variable,msg,msglen,"ALL" with a piece of redundant code
            client.send(bytes(temp, "utf8"))                                                                                                         # sending the above packed str stored in temp variable to the server over the socket


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

def allusers():
    get_thread_all_users = Thread(target=getallclients)                                                                       # initializes a thread for the function get all clients
    get_thread_all_users.start()                                                                                              # starts the above initialized thread


##############################################################################################################################################################################################################################################################################################################################
"""Function deals with getting a list of all active users from the server """
###############################################################################################################################################################################################################################################################################################################################


def getallclients():
    global allusers_list                                                                                                 # globale initializing allusers_list

    status = registered.get()                                                                                           # getting the registration of the user and storing the same in status variable
    if status == "YES":                                                                                                 # checking whether the user is a registered user or not that is status variable is "YES"
        allusers_msg = 'all_clients'                                                                                    # initializing allusers_msg to string "all_clients"  which is reserved keyword for this program
        client.send(bytes(allusers_msg, "utf8"))                                                                        # sending the allusers_msg to the server
        jsonstring1 = client.recv(BUFSIZ).decode("utf8")                                                                 # waiting for the response message from the server which will be a string form of a list containing all the users connected to the client

        if jsonstring1[0] == "[":                                                                                        # checking whether it a string form of the list of the all clients

            allusers_list = json.loads(jsonstring1)                                                                     # converting back the string to list using the json.loads fucntion
            if bool(allusers_list):                                                                                     # checking whther the list is empty or not
                concurrent_users.delete(0, tkinter.END)                                                                 # deleting all the messages inserted in the active users listbox display unit
                concurrent_users.insert(tkinter.END, "All clients\n")                                                   # inserting message Active clients into the user listbox
                for x in range(len(allusers_list)):                                                                     # traversing for the total number of users present in the list
                    concurrent_users.insert(tkinter.END, "%s\n" %allusers_list[x])                                      # inserting each username onto the all user userlist display region

                if selected == "1":                                                                                     # checking if the selected variable is "1" meaning the selection of the unicast option
                    global unicast, u                                                                                   # global initialization of unicast and u
                    unicast = tkinter.Toplevel(top)                                                                     # creating a child frame instance
                    unicast.title("UNICAST USER SELECTION")                                                             # naming the child frame
                    for x in range(len(allusers_list)):                                                                 # traverse for the number of users present in the all clients  list
                        tkinter.Radiobutton(unicast,                                                                    # creation of radio buttons for each username for the selection of username - after selection username value itself is set ontot the variable
                                            text=allusers_list[x],
                                            padx=20,
                                            variable=u,
                                            value=allusers_list[x]).pack()
                    btn1 = tkinter.Button(unicast, text="Confirm User", command=quit_unicast)                           # confirm users button to confirm and set the username selected and close the window
                    btn1.pack()                                                                                         # packing the button onto the child frame

                elif selected == "2":                                                                                   # checking if the selected variable is "2" - option selected is multicast
                    global multicast                                                                                    # gloabl initialization of variable multicast
                    multicast = tkinter.Toplevel(top)                                                                   # creating a child frame
                    multicast.title("MULTICAST USER SELECTION")                                                         # naming the child frame
                    for x in range(len(allusers_list)):                                                                 # traversing for the number os users present in the all_clients list
                        intvar_dict[allusers_list[x]] = tkinter.IntVar()                                                # setting each username from the all clients list as a key and making them tkinter intvariable
                        c = tkinter.Checkbutton(multicast, text=allusers_list[x],                                       # checkbuttons are created for the total number os all users from the list and which when selected the value is set or else it is not
                                                variable=intvar_dict[allusers_list[x]])
                        c.pack()                                                                                        # packing each checkbutton onto the child frame
                    btn1 = tkinter.Button(multicast, text="Confirm Users", command=quit_multicast)                      # confirm users button to set the users selected and close the child frame window
                    btn1.pack()                                                                                         # packing the confirm users button on to the child frame

            else:                                                                                                       # when the all clients list is empty
                concurrent_users.delete(0, tkinter.END)                                                                 # clearing all the previous inserted messages on the users listbox
                concurrent_users.insert(tkinter.END, "No User(s) Logs\n")                                               # insert a msg No active clients onto the users listbox in the frame

        else:                                                                                                           # if the received msg is not a list of all clients
            msg_list.insert(tkinter.END, jsonstring1)                                                                    # Inserting the message onto the message listbox
    exit(0)

#####################################################################################################################################################################################################################################################
"""Funcation deals with user selection of the type of messaging i.e. unicast,multicast or broadcast"""
#####################################################################################################################################################################################################################################################


def messaging_options():
    global messagingoptionframe                                                                                                 # global initializing the messagingframe variable for the child window

    status = registered.get()                                                                                                   # getting the value of the registered flag and storing it onto status
    if status == "YES":                                                                                                         # checking for a registered user -  status = "YES"
        messagingoptionframe = tkinter.Toplevel(top)                                                                            # instantiating a child frame from the main frame/ gui window
        messagingoptionframe.title("MESSAGING OPTIONS")                                                                         # naming the frame/window
        tkinter.Label(messagingoptionframe, text="""Choose a Messaging Option:""", justify=tkinter.LEFT, padx=20).pack()        # setting a label and packing the label onto the child fraem
        Radiobutton(messagingoptionframe, text='Unicast(1-to-1)', variable=v, value="1").pack()                                 # setting and packing a radiobutton selection option for unicast whose value is selected will be "1" and will be stored in the variable v
        Radiobutton(messagingoptionframe, text='Multicast(1-to-Many)', variable=v, value="2").pack()                            # setting and packing a radiobutton selection option for multicast whose value is selected will be "2" and will be stored in the variable v
        Radiobutton(messagingoptionframe, text='Broadcast(1-to-All)', variable=v, value="3").pack()                             # setting and packing a radiobutton selection option for broadcast whose value is selected will be "3" and will be stored in the variable v
        Button(messagingoptionframe, text="OK", command=quit_messaging_options).pack()                                          # setting and packing a button for the selection confirmation and forwarding the selection and window closure


################################################################################################################################################################################################################
"""function deals with the getting the message option selection & window closing  """
################################################################################################################################################################################################################3


def quit_messaging_options():
    global selected                                                             # gloabl initialization of the variable selected
    selected = v.get()                                                          # getting the value from the variable "v" from the message options frame
    messagingoptionframe.destroy()                                              # closing the messaging option frame


################################################################################################################################################################################################################
"""function deals with the getting the multicast username list & window closing  """
################################################################################################################################################################################################################3


def quit_multicast():
    for key, value in intvar_dict.items():                                      # traversing the dictionary created with values being set/unset and keys being the username
        if value.get() > 0:                                                     # checking whether the value is set or not
            multicast_list.append(key)                                          # appending the key i.e. the username which are selected in the checkboxes to the multicast list
    multicast.destroy()                                                         # closing the frame/window - multicast selection


################################################################################################################################################################################################################
"""function deals with the getting the unicast username & window closing  """
################################################################################################################################################################################################################3


def quit_unicast():
    global unicast_selection                                                    # global initializing unicast_selection variable
    unicast_selection = u.get()                                                 # getting the selection from the variable u selected in the unicast usernames selsction window
    unicast.destroy()                                                           # closing the frame/ window - unicast selection

######################################################################################################################################################################################################################################################################################################################
"""Function deals with requesting of available messages from the server"""
######################################################################################################################################################################################################################################################################################################################


def check_my_messages():
    status = registered.get()                                                                                       # getting the registered flag value onto status variable
    if status == "YES":                                                                                             # checking if status value is "YES" - meaning this is connected/registered user
        message_request = "message_request"                                                                         # initializing a message message_resuest
        client.send(bytes(message_request, "utf8"))                                                                 # sending the msg request to the server with encoding


################################################################################################################################################################################################################
""" Declaration  of global variables"""
################################################################################################################################################################################################################3


global v, u                                     # v,u used to store unicast selection and message option selection
global unicast                                  # used to create a child window instance
global activeclients_list                      # used to store the active client users got from the server
global status                                   # used to mark the registration status of the user
global allusers_list                                                                                                 # globale initializing allusers_list


################################################################################################################################################################################################################
""" Client GUI Window setup """
################################################################################################################################################################################################################3



top = tkinter.Tk()                                                                                                      # initializing a tkinter object as top
top.title("Client_2")                                                                                                   # naming the client window/frame
my_msg = tkinter.StringVar()                                                                                            # used to store the value from the username entry field - tkinter string variable object
my_msg.set("")                                                                                                          # clearing the entry field after the username entry

my_msg_entered = tkinter.StringVar()                                                                                    # variable to store specific message to the users
my_msg_entered.set("")                                                                                                  # setting the variable to ""

multicast_list = []                                                                                                     # list to store the usernames selected for the multicast messaging

u = StringVar(master=top)                                                                                               # variable used for unicast user selection
u.set("")                                                                                                               # setting the variable to ""

selected = StringVar(master=top)                                                                                        # variable used to store the messaging option selection - after the window is closed
selected.set("1")                                                                                                       # setting the variable to "1" by default

registered = StringVar(master=top)                                                                                      # variable used as a flag to inidicate the status of registration of a particular username
registered.set("NO")                                                                                                    # setting the variable to "NO" initially

unicast_selection = StringVar(master=top)                                                                               # variable used to store the unicast selected username
unicast_selection.set("")                                                                                               # setting the variable to ""

v = StringVar(master=top)                                                                                               # variable used to store the messaging option selection
v.set("1")                                                                                                              # setting the variable to "1" by default

intvar_dict = {}                                                                                                        # dictionary to store usernames as key(s) & values are set or not depending on the selection

################################################################################################################################################################################################################
""" CLIENT GUI SETUP"""
################################################################################################################################################################################################################3

messages_frame = tkinter.Frame(top)                                                                                     #initializing the tkinter frame to display everything

scrollbar = tkinter.Scrollbar(messages_frame)                                                                           # To scroll about the view screen or display
msg_list = tkinter.Listbox(messages_frame, height=25, width=100, yscrollcommand=scrollbar)                               # a listbox object from tkinter to showcase the received messages
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)                                                                      # packing the scrollbar onto the right of screen
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)                                                                     # positioning and packing of the msg listbox onto the frame
msg_list.pack()                                                                                                         # packing message list box

concurrent_users = tkinter.Listbox(messages_frame, height=25, width=20)                                                 # Creating a concurrent users list/ user log  display region to output the active users
concurrent_users.pack(side=tkinter.RIGHT)                                                                                # Positioning and packing of the users log display region

messages_frame.pack()                                                                                                   # pack all the items in the main display frame message frame
concurrent_users.insert(tkinter.END, "No User(s) Logs\n")                                                               # Inserting an offset message on to the users log/ concurrent users list display region

entry_field = tkinter.Entry(top, textvariable=my_msg)                                                                   # creating an entry field for the username entryy
entry_field.bind("<Return>", enter)                                                                                     # binding the entry field with a entry function
entry_field.pack()                                                                                                      # pakcing the entry field into the main gui frame

enter_button = tkinter.Button(top, text="Enter", command=enter)                                                         # entry button used to trigger the enter function to send the username to server
enter_button.pack()                                                                                                     # packing the enter button onto the main gui frame

disconnect_button = tkinter.Button(top, text="Disconnect", command=disconnect)                                          # disconnect button used to trigger disconnect function to disconnect the client from the erver
disconnect_button.pack()                                                                                                # packing the disconnect button onto the main gui frame

messagingoptions_button = tkinter.Button(top, text="Messaging options", command=messaging_options)                      # messaginoptions button used to trigger function messaging_options to select the type of messaging - uincast, multicast or broadcast
messagingoptions_button.pack()                                                                                          # packing the messagingoptions button onto the main gui frame

alluser_button = tkinter.Button(top, text="Select User(s)", command=allusers)                                              # alluser button used to trigger the function alluser to get the list all users from the server and display the username selection window depending on the messaging option selected
alluser_button.pack()                                                                                                   # packing the alluser button onto the main gui frame

message_to_send_button = tkinter.Button(top, text="Send Message to User(s)", command=message_to_send)                   # message_to_send_button used to trigger the function meesage to send - which prompts the user to enter a piece of message for the intended recipients
message_to_send_button.pack()                                                                                           # packing the message to send button onto the main gui frame

check_my_messages_button = tkinter.Button(top, text="Check Messages", command=check_my_messages)                        # check_my_messages_button used to trigger the function check_my_messages - which sends a request to the server to send any messages available for this client
check_my_messages_button.pack()                                                                                         # packing the message to send button onto the main gui frame



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
