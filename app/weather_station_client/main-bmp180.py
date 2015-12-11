"""Python program to be run on the RPi with BMP180 sensor."""
import datetime
import time

import Adafruit_BMP.BMP085 as BMP085
from communicateWithServer import communicateWithServer


def main():
    """Sensor program, running in infinite loop"""
    sensor = BMP085.BMP085()
    com = communicateWithServer()
    com.getUserPsw()
    date = str(datetime.datetime.now().date()) + ".txt"
    open(date, 'w+').close()

    while True:
        payload = {}
        payload['temp'] = sensor.read_temperature()
        payload['pressure'] = sensor.read_pressure()
        payload['altitude'] = sensor.read_altitude()
        payload['sealevel_pressure'] = sensor.read_sealevel_pressure()
        payload["username"] = com.deviceName
        payload["password"] = com.devicePsw
        payload["time"] = str(datetime.datetime.now())
        print payload

        try:
            com.putReadingToServer(payload)

        except Exception as error:
            print "The call putReadingToServer failed with an exception.", str(error)
            if str(datetime.datetime.now().date()) + ".txt" != date:
                open(str(datetime.datetime.now().date()) + ".txt", 'a').close()
            out_file = open(date, "a")
            out_file.write(str(payload))
            out_file.close()

        time.sleep(com.REFRESH_RATE)

if __name__ == "__main__":
    main()
