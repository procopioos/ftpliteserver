import threading
from tkinter import Tk, Label, Entry, Button

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def start_ftp_server():
    # Get the input values from the user
    host = host_entry.get()
    port = int(port_entry.get())
    user = user_entry.get()
    password = password_entry.get()
    directory = directory_entry.get()

    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, directory, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((host, port), handler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    window.withdraw()  # Hide the Tkinter window after starting the server


# Create the GUI
window = Tk()
window.title("FTP Server Configuration")

# Host
host_label = Label(window, text="Host:")
host_label.pack(pady=5)
host_entry = Entry(window)
host_entry.pack(pady=5, padx=15)

# Port
port_label = Label(window, text="Port:")
port_label.pack(pady=5)
port_entry = Entry(window)
port_entry.pack(pady=5, padx=15)

# User
user_label = Label(window, text="User:")
user_label.pack(pady=5)
user_entry = Entry(window)
user_entry.pack(pady=5, padx=15)

# Password
password_label = Label(window, text="Password:")
password_label.pack(pady=5)
password_entry = Entry(window, show="*")
password_entry.pack(pady=5, padx=15)

# Directory
directory_label = Label(window, text="Directory:")
directory_label.pack(pady=5)
directory_entry = Entry(window)
directory_entry.pack(pady=5, padx=15)

# Start FTP Server Button
start_button = Button(window, text="Start FTP Server", command=start_ftp_server)
start_button.pack(pady=5, padx=15)

window.mainloop()
