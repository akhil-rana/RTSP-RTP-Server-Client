import sys
from tkinter import Tk
from client.Client import Client

if __name__ == "__main__":

    serverAddr = sys.argv[1]
    serverPort = sys.argv[2]
    rtpPort = sys.argv[3]
    fileName = sys.argv[4]

    root = Tk()

    # Create a new client
    app = Client(root, serverAddr, serverPort, rtpPort, fileName)
    app.master.title("RTPClient")
    root.mainloop()
