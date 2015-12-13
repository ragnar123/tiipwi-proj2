import requests

ServerIPAddr = "192.168.43.188:8000"
usrPswFilePath = "pw_file.txt"

class communicateWithServer(object):
    DEFAULT_REFRESH_RATE = 10
    REFRESH_RATE = 10
    deviceName = ""
    devicePsw = ""

    def sendAuthRequest(self):
        r = requests.get('http://' + ServerIPAddr + '/signup')
        if r.status_code == 200:
            obj = r.json()
            self.deviceName = obj['username']
            self.devicePsw = obj['password']
            try:
                self.writeFile(self.deviceName, self.devicePsw)
                print "user and password have been written into a file"
            except Exception as e:
                print "Unable to write to file, error: " + str(e)
                pass
            return {'username':self.deviceName, 'password':self.devicePsw}
        else:
            print 'page unavailable, unable to fetch user and pass, try again later'

    def writeFile(self, deviceName, devicePsw):
        out_file = open(usrPswFilePath, "w+")
        out_file.write("username:" + deviceName + "\n" + "password:" + devicePsw)
        out_file.close()

    def readFile(self):
        with open(usrPswFilePath, "r") as file:
            data = file.read()
            if len(data.split("\n")) < 2:
                return ""
            self.deviceName = data.split("\n")[0].split(":")[1]
            self.devicePsw = data.split("\n")[1].split(":")[1]
        return {'username':self.deviceName, 'password':self.devicePsw}

    def getUserPsw(self):
        auth = False
        out = self.readFile()
        if out == "":
            auth = self.sendAuthRequest()
            if auth:
                print "the exit value " + str(auth) + " was fetched from a server request"
                return auth
            else:
                print "unable to get User and Password neither from file nor from server"
        else:
            print "the exit value " + str(out) + " was fetched from the file"
            return out

    def putReadingToServer(self, payload):

        url = "http://" + ServerIPAddr + "/put_reading/" + payload["username"] + "/"
        rout = requests.post(url, data=payload)
        print url
        print rout.text
        print self.deviceName
        print self.devicePsw

        if rout.status_code == 200:
            try:
                obj = rout.json()
                print obj
                if obj['refresh_interval']:
                    self.REFRESH_RATE = obj['refresh_interval']
                    print "New refresh rate is: " + str(self.REFRESH_RATE) + " default is: " + str(self.DEFAULT_REFRESH_RATE)
            except Exception as error:
                print "Exception thrown in putReadingToServer() ", str(Exception), str(error)
        else:
            self.REFRESH_RATE = self.DEFAULT_REFRESH_RATE
