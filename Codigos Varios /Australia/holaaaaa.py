
import socket
import struct
import time
 
# Create a TCP/IP socket
TCP_IP = '192.168.2.165'
TCP_PORT = 502
BUFFER_SIZE = 1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

try:
    # Ask user for Modbus options
    print("\nPLEASE ENTER MODBUS OPTIONS")
    #unitId = input(" Unit Identifier : ")
    unitId = 1
    #functionCode = input(" Function Code : ")
    functionCode = 3
    #startRegister = input(" Start Register : ")
    startRegister = 50512
    #numRegister = input(" Number of Registers : ")
    numRegister = 2
    # Construct request packet
    req = struct.pack('>3H 2B 2H', 0, 0, 6, int(unitId), int(functionCode), int(startRegister), int(numRegister))
    sock.send(req)
     # Calculate receipt packet buffer and structure
    BUFFER_SIZE = (3*2) + (3*1) + (int(numRegister)*2)
    rec = sock.recv(BUFFER_SIZE)
 
    def setB():
        global BH
        BH = 'B' #1
    def setH():
        global BH
        BH = 'H' #2
 
    functionLookup = {
        1 : setB, # Read Coils (1 byte)
        2 : setB, # Read Input Discrete Registers (1 byte)
        3 : setH, # Read Holding Registers (2 byte)
        4 : setH  # Read Input Registers (2 byte)
    }
    functionLookup[int(functionCode)]()
 
    s = struct.Struct('>3H 3B %s%s' %(numRegister, BH))
    data = s.unpack(rec)
    # Print out register values
    print("\nREGISTER VALUES")
    for i in range(6, 6+int(numRegister)):
        currentRegister = str((i - 6) + int(startRegister)).zfill(2)
        print(" Register #%s : %s" %(currentRegister, data[i]))
 
    # Wait a couple of seconds before disconnecting
    print ("data: %s"%(data[i]))
    time.sleep(2);
 
finally:
    print('\nCLOSING SOCKET')
    sock.close()
