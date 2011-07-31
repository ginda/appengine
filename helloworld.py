import shutil
import os
import time
import datetime
import math
import urllib2
import time
from array import array


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class myClass:
    @staticmethod
    def grabmyurl(url):
        loadtime=0;
        t0 = time.time()
        content = [];
        try:
            filehandle = urllib2.urlopen( url )
            for lines in filehandle.readlines():
                content.append(lines)

            filehandle.close()
        except urllib2.URLError, e:
            handleError(e)
        loadtime = time.time() - t0;
        return loadtime 



class MainPage(webapp.RequestHandler):

    def get(self):
       self.response.headers['Content-Type'] = 'text/plain'
       x = myClass()
       self.response.out.write("vd_: "+str( x.grabmyurl("http://www.vd.de") )+" seconds to load file\n")
       self.response.out.write("fb_: "+str( x.grabmyurl("http://www.fb.com") )+" seconds to load file\n")
       self.response.out.write("fb2: "+str( x.grabmyurl("http://www.fb2.com") )+" seconds to load file\n")




application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
