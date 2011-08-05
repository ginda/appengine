import urllib2
import time
from google.appengine.ext import db

class Greeting(db.Model):
    url = db.StringProperty(multiline=False)
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class myClass:
    """
    coxmment
    """    
    @staticmethod
    def grabmyurl(url):
        """
        @url: int
        Adds 3 to x
        returns an int
        """    
        t0 = time.time()
        for n in range(0, 8):
            try:
                content = [];
                filehandle = urllib2.urlopen( url )
                for lines in filehandle.readlines():
                    content.append(lines)

                filehandle.close()
            except urllib2.URLError, e:
                print(e)
        loadtime = (time.time() - t0)/8
        
        
        greeting = Greeting("tablename")

        greeting.url = url
        greeting.content = loadtime
        greeting.put()       
        return loadtime 

