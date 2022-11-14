from opcua import Client
import time

url = "opc.tcp://192.168.0.120:4840"

client = Client(url)

client.connect()
print("Client Connected")

while True:
           Temp = client.get_node("ns=4;s=|var|CPX-E-CEC-C1-EP.Application.G_HMI.AxisInfo.ActPosition")
           Temperature = Temp.get_value()
           print(Temperature)
