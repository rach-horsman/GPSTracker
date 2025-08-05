# Import necessary libraries
import serial          # Enables communication with the serial port (e.g., GPS module)
import time            # Optional: For delays or timestamping (not used in current snippet)
import string          # Optional: For string operations (not used in this code)
import pynmea2         # Library to parse NMEA sentences from GPS data

# Infinite loop to continuously read and process GPS data
while True:
    # Define the serial port for the GPS module (ttyAMA0 is typical for UART on a Raspberry Pi)
    port = "/dev/ttyAMA0"

    # Open the serial connection with the specified baudrate and timeout
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)

    # Instantiate an NMEA stream reader (not strictly necessary here)
    dataout = pynmea2.NMEAStreamReader()

    # Read one line of raw data from the serial port (NMEA sentence)
    newdata = ser.readline()

    # Decode the byte stream into a regular string using Latin-1 encoding
    n_data = newdata.decode('latin-1')

    # Check if the received NMEA sentence is of type GPRMC (Recommended Minimum Specific GPS/Transit Data)
    if n_data[0:6] == "$GPRMC":
        # Parse the GPRMC sentence to extract structured data
        newmsg = pynmea2.parse(n_data)

        # Extract latitude and longitude values
        lat = newmsg.latitude
        lng = newmsg.longitude

        # Format the extracted coordinates into a readable string
        gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)

        # Print the coordinates to the console
        print(gps)
