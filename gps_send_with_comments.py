# Import required libraries
import pyrebase         # For interacting with Firebase (Python wrapper)
import serial           # For serial communication with GPS device
import pynmea2          # For parsing NMEA GPS data strings

# Firebase configuration dictionary
firebaseConfig = {
    "apiKey": "xxxx",                # Your Firebase API key
    "authDomain": "xxxx",           # Your Firebase Auth domain
    "databaseURL": "xxxx",          # Your Realtime Database URL
    "projectId": "xxxx",            # Your Firebase project ID
    "storageBucket": "xxxx",        # (Optional) Firebase storage
    "messagingSenderId": "xxxx",    # Messaging sender ID for cloud messaging
    "appId": "xxxx",                # Unique app ID
}

# Initialize Firebase connection using the configuration
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()  # Reference to the Firebase Realtime Database

# Infinite loop to continuously read GPS data and send it to Firebase
while True:
    # Define and open the serial port connected to the GPS module
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)

    # Create a stream reader for NMEA sentences (optional here)
    dataout = pynmea2.NMEAStreamReader()

    # Read one line of data from the serial port
    newdata = ser.readline()

    # Decode the byte data into a readable string using Latin-1 encoding
    n_data = newdata.decode('latin-1')

    # Check if the line is a valid GPRMC sentence (contains GPS position)
    if n_data[0:6] == '$GPRMC':
        # Parse the sentence to extract structured GPS information
        newmsg = pynmea2.parse(n_data)

        # Extract latitude and longitude from the parsed data
        lat = newmsg.latitude
        lng = newmsg.longitude

        # Format and display the GPS coordinates
        gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
        print(gps)

        # Prepare data to send to Firebase
        data = {"LAT": lat, "LNG": lng}

        # Upload data to the Firebase Realtime Database
        db.update(data)  # ⚠️ This may fail if permissions are not set correctly in Firebase
        print("Data sent")
