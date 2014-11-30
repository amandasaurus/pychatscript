import cmd, sys, argparse
import six

from .server import ChatScriptServer

class InteractiveSession(cmd.Cmd):
    prompt = "> "

    servername = 'localhost'
    port = 1024
    botname = None
    username = None

    def connect_to_server(self):
        self.server = ChatScriptServer(self.servername, port=self.port, username=self.username, botname=self.botname)
        
    def preloop(self):
        self.connect_to_server()
        self.print_welcome_message()

    def print_welcome_message(self):
        welcome_msg = "("
        if self.port == 1024:
            welcome_msg += "You are connected to {}, ".format(self.servername)
        else:
            welcome_msg += "You are connected to {}:{}, ".format(self.server, self.port)

        if self.botname == None:
            welcome_msg += "and talking to the default bot. "
        else:
            welcome_msg += "and talking to {}. ".format(self.botname)

        welcome_msg += "Your username is {}.".format(self.username)
        welcome_msg += ")"

        six.print_(welcome_msg)

    def default(self, line):
        self.do_say(line)

    def do_say(self, line):
        response = self.server.say(line)
        six.print_(response)

    def do_EOF(self, line):
        return True

    def do_server(self, line):
        self.servername = line
        self.connect_to_server()
        six.print_("(Changed server to {})".format(line))

    def do_port(self, line):
        self.port = line
        self.connect_to_server()
        six.print_("(Changed port to {})".format(line))

    def do_botname(self, line):
        self.botname = line
        self.connect_to_server()
        six.print_("(Changed botname to {})".format(line))

    def do_username(self, line):
        self.username = line
        self.connect_to_server()
        six.print_("(Changed username to {})".format(line))

    def do_quit(self, line):
        six.print_("(Closing connection)")
        return True
    
    def emptyline(self):
        pass


def interactive_session(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", help="Server to connect to.", default="localhost")
    parser.add_argument("-p", "--port", help="Port", default=1024)
    parser.add_argument("-u", "--username", default=".")
    parser.add_argument("-b", "--botname", default=None)

    args = parser.parse_args(argv)

    session = InteractiveSession()
    session.servername = args.server
    session.port = args.port
    session.username = args.username
    session.botname = args.botname

    session.cmdloop()

if __name__ == '__main__':
    interactive_session(sys.argv[1:])
