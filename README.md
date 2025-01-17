# FTPLite Server
A lite FTP Server made in Python3. It includes a simple UI.

## How to install:
Don't panic: here's a step to step guide.<br>
Download the code from GitHub or, if you're one of those terminal guys,<br>just use git:
`git clone https://github.com/famicomm/ftpliteserver.git`

If you're one of those easy guys, I made an executable for you!

## How do I use it?
Great! If you managed to arrive here, I suppose you already downloaded it. Great job!<br>
On Windows, you can start the server just by double-clicking on the Python file.<br>
Again, if you're one of those terminal guys, it's simple:<br>
`python3 ./server.py` or `python3 /path/to/repo/server.py`<br>

Right, another thing: if you're on Windows, remember to accept any Windows Firewall notice, <br>else you won't be able to connect to the server

## Oh no! It doesn't launch!
I forgot to say that you need to install the dependencies. <br>
My fault, you're right. There:

## Dependencies
* ftplib (It should be already preinstalled in Python. if it isn't, `pip install ftplib`)
* pyftpdlib (`pip install pyftpdlib`)

There! You're all set to configure and install your very own FTP Server.

## What about TLS Support?
Don't worry, it's in the works. Anyways, you'll have to use your own TLS certificate and private key.

### What's TLS?
Think of it as an added security layer to (in this situation) your FTP server. Transport Layer Security is a protocol designed to provide communications security over a computer network. The protocol is widely used in many cases, like emails, messaging apps, voIP (Voice over IP) and HTTPS.  
