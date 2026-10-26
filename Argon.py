import platform
import serial.tools.list_ports

os_type = platform.system()
port_name = None

ports = serial.tools.list_ports.comports()
for p in ports:
    if "USB" in p.description or "CP210" in p.description or "ACM" in p.description:
        port_name = p.device
        break
# This loop here just identifies which port your on 

if port_name is None:
	print("Could not find port name") # err handle
else:
	print(f"Using port: {port_name}")
    try:
        ser = serial.Serial(port_name, 115200, timeout=1)
        if os_type == "Windows":
            ser.write(b"WINDOWS\n")
        elif os_type == "Linux":
            ser.write(b"LINUX\n")
        elif os_type == "Darwin":
        	ser.write(b"Mac\n")
        ser.close()
	# writes the code to the serial on the USB ESP 32 S3 so it knows what scripts to execute in specific.
    except Exception as e:
		# err handle
        print(f"Failed to connect: {e}")
	else:
    	print("No matching serial port found!")
   
