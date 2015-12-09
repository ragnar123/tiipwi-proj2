from SenseFromHat import SenseFromHat
from communicateWithServer import communicateWithServer
import datetime
import time

date = ""

def main():
    hat = SenseFromHat()
    com = communicateWithServer()
    usrpsw = com.getUserPsw()
    date = str(datetime.datetime.now().date()) + ".txt"
    fname = open(date, 'w+').close()

    while True:
        payload = hat.getTempHumPress()
        payload["username"] = usrpsw["username"]
        payload["password"] = usrpsw["password"]
        payload["time"] = str(datetime.datetime.now())
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

        time.sleep(com.REFRESH_RATE)

if __name__ == "__main__":
    main()
