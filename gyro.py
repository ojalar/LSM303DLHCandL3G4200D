# Based on https://github.com/ControlEverythingCommunity/L3G4200D

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# L3G4200D address, 0x68(104)
# Select Control register1, 0x20(32)
#		0x0F(15)	Normal mode, X, Y, Z-Axis enabled
bus.write_byte_data(0x69, 0x20, 0x0F)

# L3G4200D address, 0x68(104)
# Select Control register4, 0x23(35)
#		0x30(48)	Continous update, Data LSB at lower address
#					FSR 2000dps, Self test disabled, 4-wire interface

# 2000 dps
#dps_digit = 0.07
#bus.write_byte_data(0x69, 0x23, 0x30)
# 250 dps
#dps_digit = 0.00875
#bus.write_byte_data(0x69, 0x23, 0x00)
# 500 dps
dps_digit = 0.01750
bus.write_byte_data(0x69, 0x23, 0x10)

time.sleep(0.5)

x_cum = 0
y_cum = 0
z_cum = 0

t_l = time.time()

while True:
    # L3G4200D address, 0x68(104)
    # Read data back from 0x28(40), 2 bytes, X-Axis LSB first
    data0 = bus.read_byte_data(0x69, 0x28)
    data1 = bus.read_byte_data(0x69, 0x29)

    # Convert the data
    xGyro = data1 * 256 + data0
    if xGyro > 32767 :
            xGyro -= 65536

    # L3G4200D address, 0x68(104)
    # Read data back from 0x2A(42), 2 bytes, Y-Axis LSB first
    data0 = bus.read_byte_data(0x69, 0x2A)
    data1 = bus.read_byte_data(0x69, 0x2B)

    # Convert the data
    yGyro = data1 * 256 + data0
    if yGyro > 32767 :
            yGyro -= 65536

    # L3G4200D address, 0x68(104)
    # Read data back from 0x2C(44), 2 bytes, Z-Axis LSB first
    data0 = bus.read_byte_data(0x69, 0x2C)
    data1 = bus.read_byte_data(0x69, 0x2D)

    # Convert the data
    zGyro = data1 * 256 + data0
    if zGyro > 32767 :
            zGyro -= 65536
    
    t_c = time.time()
    dt = t_c - t_l
    t_l = t_c

    x_cum += xGyro*dps_digit*dt
    y_cum += yGyro*dps_digit*dt
    z_cum += zGyro*dps_digit*dt
    
    # Output data to screen
    print("Rotation in X-Axis : %f" %x_cum)
    print("Rotation in Y-Axis : %f" %y_cum)
    print("Rotation in Z-Axis : %f" %z_cum)
