#https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox
'''
For creating GUI applications on Ubuntu, you can refer to the documentation of popular graphical toolkits that are commonly used on Linux systems. Here are some resources for creating GUI applications on Ubuntu:

GTK (GIMP Toolkit):

Official documentation: GTK Documentation
Tutorial: GTK 3 Tutorial
Qt:

Official documentation: Qt Documentation
Tutorial: Qt5 Python GUI Programming Cookbook
Tkinter (Python's built-in GUI toolkit):

Official documentation: Tkinter Documentation
Tutorial: Tkinter Tutorial
PyGTK (Python bindings for GTK):

Tutorial: PyGTK Tutorial
PyQt (Python bindings for Qt):

Tutorial: PyQt Tutorial'''



import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def show_message_box(message):
    dialog = Gtk.MessageDialog(
        transient_for=None,
        flags=0,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text=message
    )
    dialog.run()
    dialog.destroy()

# Example usage
message = "Hey Gaurav !! \nif you see this message that means your code is working"
show_message_box(message)




