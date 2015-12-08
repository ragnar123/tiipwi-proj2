import weather_station_client.SenseFromHat
import weather_station_client.communicateWithServer
import datetime
import time


date = ""

def __init__(self):
    hat = SenseFromHat()
    com = communicateWithServer()
    com.getUserPsw()
    self.date = datetime.date()
    fname = open(date, 'w+').close()

def main(self):
    while True:
        payload = hat.getTempHumPress()
        payload = payload + {'time': str(datetime.datetime.now())}

        try:
            com.putReadingToServer(payload)
        except Exception:
            if (!(datetime.date()==self.date)):
                fname = open(datetime.date(), 'a').close()
            out_file = open(fname,"a")
            out_file.write(payload + '\n')
            out_file.close()

        sleep(REFRESH_RATE)

if __name__ == "__main__":
    main()
