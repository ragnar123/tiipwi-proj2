from weather_station.models import SensorNode



class Reading(enum):


class dataAnalysis:

        def findTempReading(self, value1, value2 , startLat, startLon, endLat, endLon, date):
            resultsList = SensorNode.objects.filter(timestamp=datetime.date(date), )

            #todo: figure out how to retrieve the values in the database belonging inside a specifical area
        def findLightReading

        def findWindReading

        def plotCurvesOnMap
