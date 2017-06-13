import nfc
import binascii
import hashlib
import urllib
import urllib2


def setCardID(tag):
    idm = binascii.hexlify(tag.idm)
    url = "url"
    params = {"cardid": hashlib.sha1(idm).hexdigest()}
    params = urllib.urlencode(params)
    
    req = urllib2.Request(url)
    req.add_data(params)
    
    res = urllib2.urlopen(req)
    r = res.read()
    print('ok')
    return idm

clf = nfc.ContactlessFrontend('usb:001:004')
cardid = clf.connect(rdwr={'on-connect': setCardID})
#print(idm)
clf.close()
