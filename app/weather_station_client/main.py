from communicateWithServer import communicateWithServer

print "helo"

instance = communicateWithServer()

print instance
pw = instance.getUserPsw()
print pw.username

# Find connected sensors


instance.putReadingToServer()

