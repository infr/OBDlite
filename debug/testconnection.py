import serial
import serial.tools.list_ports
import time

print serial.tools.list_ports.comports()


raw_input("Press Enter to continue...")

ser = serial.Serial('/dev/cu.OBDII-SPP')
print(ser.name)
ser.write('atz')
s = ser.read(1)
print s
ser.close()


raw_input("Press Enter to continue...")

with serial.Serial('/dev/tty.OBDII-SPP') as ser:
	ser.write('atz')
#	line = ser.readline()

	time.sleep(0.1)
	buffer = ""
	while 1:
		c = ser.read(1)
		if c == '\r' and len(buffer) > 0:
	 		break
	 	else:
	 		if buffer != "" or c != ">": #if something is in buffer, add everything
	 			buffer = buffer + c
 		print "%s says %s" % (ser.name, line)