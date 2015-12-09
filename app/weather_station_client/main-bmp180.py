from communicateWithServer import communicateWithServer
import Adafruit_BMP.BMP085 as BMP085
import datetime
import time


REFRESH_RATE = 10

date = ""

def main():
    sensor = BMP085.BMP085()
    com = communicateWithServer()
    usrpsw = com.getUserPsw()
    date = str(datetime.datetime.now().date()) + ".txt"
    fname = open(date, 'w+').close()

    while True:
        payload = {
                'temp': sensor.read_temperature(),
                'pressure': sensor.read_pressure(),
                'altitude': sensor.read_altitude(),
                'sealevel_pressure': sensor.read_sealevel_pressure() };
        payload["username"] = usrpsw["username"]
        payload["password"] = usrpsw["password"]
        payload["time"] = str(datetime.datetime.now())
        payload["lat"] = -1
        payload["lon"] = -1
        payload["light"] = -1
        payload["wind_speed"] = -1
        print payload

        try:
            com.putReadingToServer(payload)

        except Exception as error:
            print "The call putReadingToServer failed with an exception.", str(error)
            if (not(str(datetime.datetime.now().date()) + ".txt"==date)):
                fname = open(str(datetime.datetime.now().date()) + ".txt", 'a').close()
            out_file = open(date,"a")
            out_file.write(str(payload))
            out_file.close()

        time.sleep(REFRESH_RATE)

if __name__ == "__main__":
    main()
