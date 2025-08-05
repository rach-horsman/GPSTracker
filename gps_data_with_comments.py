# Importing required libraries
import serial          # For serial communication with the GPS module
import time            # Optional: For adding delays or timestamps (not used in current code)
import string          # Optional: For handling strings (not used in current code)
import pynmea2         # For parsing NMEA sentences from GPS

# Infinite loop to continuously read data from the GPS module
while True:
    port = "/dev/ttyAMA0"  # Define the serial port to which the GPS module is connected (typical for Raspberry Pi)
    
    # Initialize serial communication with the GPS module
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    
    # Create an NMEA stream reader object (not actively used in this snippet)
    dataout = pynmea2.NMEAStreamReader()
    
    # Read one line of data from the serial port
    newdata = ser.readline()
    
    # Decode the byte string into a readable string using Latin-1 encoding
    n_data = newdata.decode('latin-1')
    
    # Print the decoded NMEA sentence to the console
    print(n_data)
