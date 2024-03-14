import pylink
'''
need copy JlinkARM.dll JLink_x64.dll to windows/system32
'''

# Create jlink object
jlink = pylink.JLink()

#jlink.open(serial_no=59409806)

# Open J-Link 
jlink.open()

# Get serial_number
print('Serial number:',jlink.serial_number)
print("prodect_name:", jlink.product_name)

jlink.set_tif(pylink.enums.JLinkInterfaces.JTAG)

jlink.connect('STM32F103C8')

if jlink.target_connected():
    print("Success connect to target device") 
else:
    print("Fail to connect to target device")

data = jlink.memory_read8(0, 1024)

# Read data from memory
print("Read data from memory:")
print(data)

# Disconnect from J-Link
jlink.close()