# creating customised Burpsuite extension in python

'''
https://portswigger.net/burp/communitydownload
https://www.jython.org/download  (Jython Standalone: Use this to run Jython without installing or to embed Jython in a Java application. (metadata))
https://github.com/securityMB/burp-exceptions/


first open one more vscode window run un_ebs.py then run the this burp extension(bind shell) in burp suite
'''


from burp import IBurpExtender , ITab
from javax import swing
from java.awt import BorderLayout
import sys , time, socket,threading,sys
from exceptions_fix import FixBurpExceptions
from javax.swing import BorderFactory

class BurpExtender(IBurpExtender, ITab):
    def registerExtenderCallbacks(self,callbacks):
        self.clicked = False
        self.response_data = None
        self.kill_threads = False

        sys.stdout = callbacks.getStdout()
        
        self.callbacks = callbacks

        self.callbacks.setExtensionName("Bind shell")

        self.tab = swing.JPanel(BorderLayout())

        text_panel = swing.JPanel()
        box_vertical = swing.Box.createVerticalBox()

    

        box_horizontal = swing.Box.createHorizontalBox()
        self.ip_address = swing.JTextArea('', 2,100)
        self.ip_address.setLineWrap(True)
        self.ip_address.border = swing.BorderFactory.createTitledBorder("IP Address:")
        box_horizontal.add(self.ip_address)
        box_vertical.add(box_horizontal)

        box_horizontal = swing.Box.createHorizontalBox()
        self.user_command = swing.JTextArea('' , 2,100)
        self.user_command.setLineWrap(True)
        self.user_command.border = swing.BorderFactory.createTitledBorder("command:")
        box_horizontal.add(self.user_command)
        box_vertical.add(box_horizontal)

        box_horizontal = swing.Box.createHorizontalBox()
        button_panel = swing.JPanel()

        self.connect_button = swing.JButton('[ --- Connect --- ]', actionPerformed=self.connect)
        self.send_button = swing.JButton('[ --- Send Command ---]', actionPerformed=self.send)
        self.disconnect_button = swing.JButton('[ --- Disconnect --- ]', actionPerformed=self.disconnect)

        self.disconnect_button.enabled = False
        self.send_button.enabled = False

        button_panel.add(self.connect_button)
        button_panel.add(self.send_button)
        button_panel.add(self.disconnect_button)
        
        box_horizontal.add(button_panel)
        box_vertical.add(box_horizontal)

        box_horizontal = swing.Box.createHorizontalBox()
        self.output = swing.JTextArea('', 25,100)
        self.output.setLineWrap(True)
        self.output.setEditable(False)

        scroll = swing.JScrollPane(self.output)

        box_horizontal.add(scroll)
        box_vertical.add(box_horizontal)

        
        text_panel.add(box_vertical)

        self.tab.add(text_panel)

        callbacks.addSuiteTab(self)
        return
    
    def getTabCaption(self):
        return "Bind shell"
    
    def getUiComponent(self) :
        return self.tab
    
    def send(self, event):
        if self.clicked:
            self.output.text = self.response_data
            self.clicked = False  # Reset the flag after displaying the response data
        else:
            self.output.text = "No data received"

    def send_thread(self):
        while True:
            if self.kill_threads:
                sys.exit()

            if self.clicked:
                self.clicked = False
                self.s.send(self.user_command.text)

    def recv_thread(self):

        while True:
            if self.kill_threads:
                sys.exit()

            data = self.s.recv(4096).decode("utf-8")
            if not data:
                self.response_data = "No data received"
            else:
                self.response_data = data.strip()
            # Additional print statements for debugging
            print("Clicked:", self.clicked)
            print("Response data:", repr(self.response_data))

    def connect(self, event):
        try :
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.ip_address.text,1234))
            self.kill_threads = False

            threading.Thread(target=self.send_thread).start()
            threading.Thread(target=self.recv_thread).start()

            self.connect_button.enabled = False
            self.disconnect_button.enabled = True
            self.send_button.enabled = True
            self.ip_address.enabled = False
            
            self.output.text  = "Connected to bind shell!"
            
        except:
            self.output.text = "Could not connect, try again!"

    
    def disconnect(self , event):
        self.s.send("exit")
        self.s.close()
        self.kill_threads = True

        self.connect_button.enabled = True
        self.disconnect_button.enabled = False
        self.send_button.enabled = False
        self.ip_address.enabled = True
        self.output.text = "Disconnected from bind shell!"
        

FixBurpExceptions()