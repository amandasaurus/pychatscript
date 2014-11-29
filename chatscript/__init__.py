# -*- coding: utf-8 -*-

__author__ = 'Rory McCann'
__email__ = 'rory@technomancy.org'
__version__ = '0.1.0'

import socket
import cmd

class ChatScriptServer(object):
    def __init__(self, servername, port=1024, username=None, botname=None):
        self.servername = servername
        self.port = port
        self.username = username or '.'
        self.botname = botname or ''

    def say(self, message):
        to_say = "{username}\0{botname}\0{message}\0".format(username=self.username, botname=self.botname, message=message)

        connection = socket.create_connection((self.servername, self.port))

        connection.send(to_say)
        response =  ""
        while True:
            chunk = connection.recv(100)
            if chunk:
                response += chunk
            else:
                break

        return response

class InteractiveSession(cmd.Cmd):
    prompt = "> "

    server = 'localhost'
    port = 1024
    botname = None
    username = None

    def connect_to_server(self):
        self.server = ChatScriptServer("localhost", port=self.port, username=self.username, botname=self.botname)
        
    def preloop(self):
        self.connect_to_server()

    def default(self, line):
        response = self.server.say(line)
        print response

    def do_EOF(self, line):
        return True

    def do_server(self, line):


InteractiveSession().cmdloop()
