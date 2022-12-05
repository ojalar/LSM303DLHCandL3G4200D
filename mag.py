# Based on https://github.com/ControlEverythingCommunity/LSM303DLHC

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

bus.write_byte_data(0x1e, 0x02, 0x00)
bus.write_byte_data(0x1e, 0x00, 0x10)


time.sleep(0.5)


while True:
    # L3G4200D address, 0x68(104)
    # Read data back from 0x28(40), 2 bytes, X-Axis LSB first
    data0 = bus.read_byte_data(0x1e, 0x03)
    data1 = bus.read_byte_data(0x1e, 0x04)

    # Convert the data
    xGyro = data1 * 256 + data0
    if xGyro > 32767 :
            xGyro -= 65536

    # L3G4200D address, 0x68(104)
    # Read data back from 0x2A(42), 2 bytes, Y-Axis LSB first
    data0 = bus.read_byte_data(0x1e, 0x07)
    data1 = bus.read_byte_data(0x1e, 0x08)

    # Convert the data
    yGyro = data1 * 256 + data0
    if yGyro > 32767 :
            yGyro -= 65536

    # L3G4200D address, 0x68(104)
    # Read data back from 0x2C(44), 2 bytes, Z-Axis LSB first
    data0 = bus.read_byte_data(0x1e, 0x05)
    data1 = bus.read_byte_data(0x1e, 0x06)

    # Convert the data
    zGyro = data1 * 256 + data0
    if zGyro > 32767 :
            zGyro -= 65536
     
    # Output data to screen
    print("Rotation in X-Axis : %f" %(xGyro/32768))
    print("Rotation in Y-Axis : %f" %(yGyro/32768))
    print("Rotation in Z-Axis : %f" %(zGyro/32768))
