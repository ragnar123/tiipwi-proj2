import requests

global DEFAULT_REFRESH_RATE = 1000
global REFRESH_RATE = 1000
global ServerIPAddr = "localhost:8000"
global usrPswFilePath = ""
global deviceName = ""
global devicePsw = ""

class communicateWithServer(object):

    def sendAuthRequest(self):
        r = requests.get('https://' + ServerIPAddr + '/signup')
        if (r.status_code==200){
            obj = r.json()
            deviceName = obj['username']
            devicePsw = obj['password']

            try:
                writeFile()
            except Exception:
                pass
            }
        else:
            console.log('page unavailable')

    def writeFile(self):
        out_file = open(usrPswFilePath,"w+")
        out_file.write("username:" + deviceName + "\npassword:" + devicePsw)
        out_file.close()

    def readFile(self):
        with open (usrPswFilePath, "r") as file:
            data=file.read()
            deviceName = data.split("\n")[0].split(":")[1]
            devicePsw = data.split("\n")[1].split(":")[1]
        return file

    def getUserPsw(self):
        file = readFile()
        if(!file):
            sendAuthRequest()

    def putReadingToServer(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        rout = requests.post("http://" + ServerIPAddr + "/" + deviceName + "/", data=payload)
        print(r.text)
        rin = requests.get("http://" + ServerIPAddr + "/" + deviceName + "/"
        if (r.status_code==200){
            obj = rin.json()
            REFRESH_RATE= obj['refresh_interval']
        else:
            REFRESH_RATE = DEFAULT_REFRESH_RATE






# TODO: fetch new config; delete entry from db
