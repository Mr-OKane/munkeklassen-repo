from serial.tools import list_ports
import pydobot
import math


ports = [p.device for p in list_ports.comports()]


for i, port in enumerate(ports):
    print(f"{i}: {port}")

port = ports[int(input("Vælg en port: "))]

try:
    dobot = pydobot.Dobot(port=port)
except:
    print("Fejl, kunne ikke forbinde til robotten")
print("Forbindelse oprettet")





def home():
    mode=pydobot.enums.PTPMode.MOVJ_XYZ
    dobot._set_ptp_cmd(250, 0, 150, 90, mode=mode, wait=True)

def firkantWithLines(x,y,w,h):
    dobot.move_to(x, y, -51, 0, wait = True)
    dobot.move_to(x, y+h, -51, 0, wait = True)
    dobot.move_to(x+w, y+h, -51, 0, wait = True)
    dobot.move_to(x+w, y, -51, 0, wait = True)
    dobot.move_to(x, y, -51, 0, wait = True)

def circle(v):
    for v in range(0,360,5):
        dobot.move_to(30*math.cos(v*2*math.pi/360)+300, 30*math.sin(v*2*math.pi/360), -51, 0, wait = True)
def diamond(x,y,w,h,wf,hf):
    #wf = Width forhold
    #hf = Height forhold
    dobot.move_to(x,y,-51,0, wait = True)
    dobot.move_to(x+(wf),y+(hf/2),-51,0, wait = True)
    dobot.move_to(x+(wf),y,-51,0, wait = True)
    dobot.move_to(x,y+(hf),-51,0, wait = True)
    dobot.move_to(x-(wf),y+(hf/2),-51,0, wait = True)
    dobot.move_to(x,y,-51,0, wait = True)

done = False

while done == False:
    cmd = input("Vælg kommando: ")

    if cmd.startswith("q"):
        dobot.close()
        done = True
    elif cmd == "Home":
        home()

    elif cmd == "Firkant":
        firkantWithLines(250,100,10,10)

    elif cmd =="pos":
        print(dobot.pose())

    elif cmd == "Trekant":
        dobot.move_to(250, 0, -51, 0, wait = True)
        dobot.move_to(260, 10, -51, 0, wait = True)
        dobot.move_to(260, 0, -51, 0, wait = True)
        dobot.move_to(250, 0, -51, 0, wait = True)

    elif cmd == "Firkant with lines":
        dobot.move_to(250, 0, -51, 0, wait = True)
        dobot.move_to(250, 10, -51, 0, wait = True)
        dobot.move_to(260, 10, -51, 0, wait = True)
        dobot.move_to(260, 0, -51, 0, wait = True)
        dobot.move_to(250, 0, -51, 0, wait = True)
        dobot.move_to(260, 10, -51, 0, wait = True)
        dobot.move_to(250, 10, -51, 0, wait = True)
        dobot.move_to(260, 0, -51, 0, wait = True)

    elif cmd == "Circle":
        circle(1)
    elif cmd == "Diamant":
        diamond(250,10,100,50,20,20)
