import requests

DEFAULT_REFRESH_RATE = 1000
REFRESH_RATE = 1000
ServerIPAddr = "192.168.5.111:8000"
usrPswFilePath = "pw_file.txt"
deviceName = "12112t"
devicePsw = "password_-"

class communicateWithServer(object):

    def sendAuthRequest(self):
        r = requests.get('http://' + ServerIPAddr + '/signup')
        if (r.status_code==200):
            obj = r.json()
            print obj
            deviceName = obj['username']
            devicePsw = obj['password']
            try:
                writeFile(obj['username'], obj['password'])
                print "user and password written into a file"
            except Exception:
                print "Unable to write to file" + usrPswFilePath
                pass
            return {'username':deviceName, 'password':devicePsw}
        else:
            print('page unavailable, unable to fetch user and pass, try again later')

    def writeFile(self, deviceName, devicePsw):
        print "1"
        out_file = open(usrPswFilePath,"w+")
        print "2"
        out_file.write("username:" + deviceName + "\n" + "password:" + devicePsw)
        out_file.close()
        print "Wrote to outfile : " + usePswFilePath

    def readFile(self):
        with open (usrPswFilePath, "r") as file:
            data=file.read()
            if len(data.split("\n")) < 2:
                raise Exception("PW file not valid.")
            deviceName = data.split("\n")[0].split(":")[1]
            devicePsw = data.split("\n")[1].split(":")[1]
        return {'username':deviceName, 'password':devicePsw}

    # returns a KeyPair
    def getUserPsw(self):
        try:
            return self.readFile()
        except IOError, Exception:
            print "User does not exist locally. Contactcing server."
            auth = self.sendAuthRequest()
            if auth:
                return auth
            else:
                 print "unable to get User and Password"

    def putReadingToServer(self, payload):

        url = "http://" + ServerIPAddr + "/put_reading/" + deviceName +"/"
        rout = requests.post(url, data=payload)
        print(rout.text)       

        if rout.status_code == 200:
            try:
                obj = rout.json()
                REFRESH_RATE= obj['refresh_interval']
            except Exception as error:
                print "Exception thrown in putReadingToServer() ", str(Exception), str(error)
        else:
            REFRESH_RATE = DEFAULT_REFRESH_RATE



# TODO: fetch new config; delete entry from db
