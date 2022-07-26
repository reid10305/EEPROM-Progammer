# EEPROM-Progammer
Arduino EEPROM programmer
Arduino code is adapted from the code created by Ben Eater under an MIT License. The original code 
can be found at the following URL, along with any other details about the original code:
    https://github.com/beneater/eeprom-programmer
    
The adapted version solely adds the ability to recieve the data to be written to the EEPROM via
the serial interface built into the Arduino. The data is passed over the serial interface by 
Sender.py. 

Sender.py should be executed via the command line, and takes two parameters before transmitting
any data. The first is the path to the binary file where the data intended to be sent is stored.
The data should be stored as raw binary. The second parameter is the serial port on which to
write the data to. This port can be listed with the 'COM' prefix, or just simply a valid integer 
corresponding to a valid port on the host computer. If there is no valid port corresponding to the 
input, the script print an error and terminate. 

After obataining both parameters, the script will immediatley being sending data over the port to 
the Arduino. When all of the data is sent, the script will terminate. 

The Arduino script is intended, and tested, for use on an Arduino Nano. The python script has been
developed for use on a Windows machine. There are currently no plans for MacOS or Linux development,
as of 07/2022.
