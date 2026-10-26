import platform
import serial.tools.list_ports

os_type = platform.system()
port_name = None

ports = serial.tools.list_ports.comports()
for p in ports:
    if "USB" in p.description or "CP210" in p.description or "ACM" in p.description:
        port_name = p.device
        break
        
if port_name is None:
	print("Could not find port name")
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
    except Exception as e:
        print(f"Failed to connect: {e}")
	else:
    	print("No matching serial port found!")
   
