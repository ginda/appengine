import urllib2
import time
from google.appengine.ext import db

class Lasttime(db.Model):
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
        
        # STore results in Database now
        lasttime = Lasttime(  db.Key.from_path('Lasttime', 'default_lt') ) #gleicher name wie klasse oben fuer tabelle!
        lasttime.url = url
        lasttime.content = str(loadtime)
        lasttime.put()       
        
        #and return result now
        return loadtime


    @staticmethod
    def dbreadmyurl(url):
        # FROM referenziert wieder auf Klasse oben und gibt entpsrechende refs zurück!
        lasttimes = db.GqlQuery("SELECT * "
            "FROM Lasttime " 
            "WHERE url = '"+url+"' "
            "ORDER BY date DESC LIMIT 1")

        for lasttime in lasttimes:
            return lasttime.content
        
        


#http://stackoverflow.com/questions/5365454/why-does-this-fail-google-appengine-datastore-python