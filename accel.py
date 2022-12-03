import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

bus.write_byte_data(0x19, 0x20, 0x27)
bus.write_byte_data(0x19, 0x23, 0x00)


time.sleep(0.5)


while True:
    # L3G4200D address, 0x68(104)
    # Read data back from 0x28(40), 2 bytes, X-Axis LSB first
    data0 = bus.read_byte_data(0x19, 0x28)
    data1 = bus.read_byte_data(0x19, 0x29)

    # Convert the data
    xGyro = data1 * 256 + data0
    if xGyro > 32767 :
            xGyro -= 65536

    # L3G4200D address, 0x68(104)
    # Read data back from 0x2A(42), 2 bytes, Y-Axis LSB first
    data0 = bus.read_byte_data(0x19, 0x2A)
    data1 = bus.read_byte_data(0x19, 0x2B)

    # Convert the data
    yGyro = data1 * 256 + data0
    if yGyro > 32767 :
            yGyro -= 65536

    # L3G4200D address, 0x68(104)
    # Read data back from 0x2C(44), 2 bytes, Z-Axis LSB first
    data0 = bus.read_byte_data(0x19, 0x2C)
    data1 = bus.read_byte_data(0x19, 0x2D)

    # Convert the data
    zGyro = data1 * 256 + data0
    if zGyro > 32767 :
            zGyro -= 65536
     
    # Output data to screen
    print("Rotation in X-Axis : %f" %(xGyro*6e-5))
    print("Rotation in Y-Axis : %f" %(yGyro*6e-5))
    print("Rotation in Z-Axis : %f" %(zGyro*6e-5))
