import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import json
import os

# determine if application is a script file or frozen exe
config_path = ''
if getattr(sys, "frozen", False):
    config_path = os.path.dirname(sys.executable)
elif __file__:
    config_path = os.path.join(
        os.path.dirname(__file__), "../dist/"
    )
config_path = f'{config_path}/config.json'
app = tk.Tk()
app.geometry('400x300')
app.title('Configurações do Posto')

frame = Frame(app)
frame.pack()

centerFrame = Frame(app)
centerFrame.place(anchor='c', relx = 0.5, rely=0.4)

bottomframe = Frame(app)
bottomframe.pack(side = BOTTOM)

if (os.path.exists(config_path)):
    with open(config_path) as config_file:
        config = json.load(config_file)
else:
    config = {"network": {"ip":'', "port":''}, "id":''}
    with open(config_path, 'w') as outfile:  
        json.dump(config, outfile)

ip = config["network"]["ip"]
port = config["network"]["port"]
id = config["id"] 

ipLabel = Label(centerFrame, text="IP: ") 
ipLabel.pack()
IP = Entry(centerFrame, bd =3)
IP.insert(END, ip)
IP.pack(pady=5)

portLabel = Label(centerFrame, text="Porta: ")
portLabel.pack()
PORT = Entry(centerFrame, bd =3)
PORT.insert(END, port)
PORT.pack(pady=5)

idLabel = Label(centerFrame, text="ID: ")
idLabel.pack()
ID = Entry(centerFrame, bd =3)
ID.insert(END, id)
ID.pack(pady=5)

def submit():
    confirmation = askquestion("Question", "Salvar Configurações?")
    if (confirmation == "yes"):
        config = {"network": {"ip": "", "port": ""},"id": ""}
        config["network"]["ip"] = IP.get()
        config["network"]["port"] = PORT.get()
        config["id"] = ID.get()
        with open(config_path, "w") as config_file:
            json.dump(config, config_file)

cancelButton = tk.Button(bottomframe, text ="Cancelar", command = exit)
cancelButton.pack(side = RIGHT, pady=10)

saveButton = tk.Button(bottomframe, text ="Salvar", command = submit)
saveButton.pack(side = LEFT, pady=10)

app.mainloop()