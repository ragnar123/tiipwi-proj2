from sense_hat import SenseHat

class SenseFromHat(object):
    sense = SenseHat()

    def getTempHumPress(self):
        temp = self.sense.get_temperature()
        humidity = self.sense.get_humidity()
        pressure = self.sense.get_pressure()
        print("Temp: %s Celsius\nHumidity: %s %%\nPressure: %s Millibars"%(temp,humidity,pressure))

        return {'temp':temp, 'humidity':humidity ,'pressure':pressure }
