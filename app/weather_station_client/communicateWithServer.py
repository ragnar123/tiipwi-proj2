import requests

DEFAULT_REFRESH_RATE = 1000
REFRESH_RATE = 1000
ServerIPAddr = "192.168.5.55:8000"
usrPswFilePath = "pw_file.txt"
deviceName = "1003"
devicePsw = "password_-"

class KeyPair():
    def __init__(self, username, password):
        self.username = username
        self.password = password

class communicateWithServer(object):

    def sendAuthRequest(self):
        r = requests.get('http://' + ServerIPAddr + '/signup')
        if (r.status_code==200):
            obj = r.json()
            return KeyPair(obj['username'], obj['password'])

            try:
                writeFile(obj['username'], obj['password'])
            except Exception:
                print "Unable to write to file" + usrPswFilePath
                pass
        else:
            print('page unavailable')

    def writeFile(self, deviceName, devicePsw):
        out_file = open(usrPswFilePath,"w+")
        out_file.write("username:" + deviceName + "\npassword:" + devicePsw)
        out_file.close()
        print "Wrote to outfile : " + usePswFilePath

    def readFile(self):
        with open (usrPswFilePath, "r") as file:
            data=file.read()
            deviceName = data.split("\n")[0].split(":")[1]
            devicePsw = data.split("\n")[1].split(":")[1]
        return KeyPair(deviceName, devicePsw)

    # returns a KeyPair
    def getUserPsw(self):
        try:
            file = self.readFile()
            return file
        except IOError:
            print "User does not exist locally. Contactcing server."
            auth = self.sendAuthRequest()
            return auth

    def putReadingToServer(self, payload):
        #rout = requests.post("http://" + ServerIPAddr + "/put_reading/" + deviceName + "/", data=payload)
        #print(rout.text)

	url = "http://" + ServerIPAddr + "/put_reading/" + deviceName + "/temperature/22.4/"
        rin = requests.get(url)

	print url
        if rin.status_code == 200:
            try:
                obj = rin.json()
                REFRESH_RATE= obj['refresh_interval']
            except Exception as error:
                print "Exception thrown in putReadingToServer() ", str(Exception), str(error)
        else:
            REFRESH_RATE = DEFAULT_REFRESH_RATE



# TODO: fetch new config; delete entry from db
