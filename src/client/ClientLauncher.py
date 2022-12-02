import sys, os
from tkinter import Tk

sys.path.append(os.path.abspath(os.getcwd() + "/src"))

from Client import Client


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
