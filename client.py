import socket
import tqdm
import os


SEP = "<SEP>"
BUFFER_SIZE = 4096

def X_is_running():
    from subprocess import Popen, PIPE
    p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
    p.communicate()
    return p.returncode == 0

if X_is_running():
    import PySimpleGUI as psg
    layout = [
        [psg.Text("Destination Host: "), psg.InputText(key='HOST_IN')],
        [psg.Text("Destination Port: "), psg.InputText(key='PORT_IN')],
        [psg,Text("Choose a file: "), psg.F]
    ]


host = None
port = 5001
