from contextlib import nullcontext
import serial 
import numpy as np
import time

def write_to_serial(x, arduino):
    arduino.write(bytes(x))
    return True

if __name__ == '__main__':
    ''' run on startup '''
    arduino = nullcontext
    bfile = input('Binary File Path: ')
    comport = input('comport: ')
    if not('COM' in comport):
        comport = 'COM' + comport 
    try:
        arduino = serial.Serial(port=comport, baudrate=57600, timeout=.1)
    except serial.SerialException:
        print("No device on " + comport + '.')
        raise SystemExit

    dtype = np.dtype('B')
    with open(bfile, 'rb') as file:
        npbytes = np.fromfile(file, dtype)
        
        print("Sending", end = '')
        for idx, byte in enumerate(npbytes):
            write_to_serial(byte, arduino)
            #time.sleep(0.1)
            if idx % 1024 == 0:
                print('.', end='')
    
    print(" Done!")
    file.close()